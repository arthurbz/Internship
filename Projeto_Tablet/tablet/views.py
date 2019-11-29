import random
import string
import uuid
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from . forms import PessoaForm, SenhaForm
from . models import Pessoa, TokenUsuario
from . nome_utils import gerar_nome
from . cpfs_utils import gerar_cpf
from datetime import datetime, timedelta
from django.core.mail import send_mail


def cria_pessoa(request):
    context = {}

    form = PessoaForm()

    if request.method == 'POST':
        form = PessoaForm(request.POST)
        form.save()
        return redirect('tablet:index')

    context['form'] = form

    return render(request, 'tablet/index.html', context)


@api_view(['POST'])
@parser_classes((JSONParser,))
def consulta_matricula(request):
    dado = request.data.get('dado')

    pessoa_cpf = Pessoa.objects.filter(cpf=dado)
    pessoa_matricula = Pessoa.objects.filter(matricula=dado)

    if pessoa_cpf:
        pessoas = pessoa_cpf
    elif pessoa_matricula:
        pessoas = pessoa_matricula
    else:
        return Response({}, status=404)

    pessoas_dict = []
    for pessoa in pessoas:
        pessoas_dict.append({
            'pk': pessoa.pk,
            'nome': pessoa.nome,
            'sobrenome': pessoa.sobrenome,
            'matricula': pessoa.matricula,
            'cpf': pessoa.cpf,
            'email': pessoa.email
        })

    return Response({'pessoas': pessoas_dict})


@api_view(['POST'])
@parser_classes((JSONParser,))
def get_lista_cpfs(request):
    pk = request.data.get('pk')
    pessoa = get_object_or_404(Pessoa, pk=pk)
    posicao_correto = random.randint(0, 3)
    pessoas_dict = []
    for qtd_pessoa in range(4):
        if posicao_correto != qtd_pessoa:
            pessoas_dict.append({'cpf': gerar_cpf(), 'correto': False})
        else:
            pessoas_dict.append({'cpf': pessoa.cpf, 'correto': True})
    return Response({'pessoas': pessoas_dict})


@api_view(['POST'])
@parser_classes((JSONParser,))
def get_lista_nomes(request):
    pk = request.data.get('pk')
    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoas_dict = []
    posicao_correto = random.randint(0, 3)
    for qtd_pessoa in range(4):
        if posicao_correto != qtd_pessoa:
            pessoas_dict.append({'nome': gerar_nome(), 'correto': False})
        else:
            pessoas_dict.append({'nome': pessoa.nome + " " + pessoa.sobrenome, 'correto': True})
    return Response({'pessoas': pessoas_dict})


@api_view(['POST'])
@parser_classes((JSONParser,))
def socilicitar_reset(request):
    pk = request.data.get('pk')
    pessoa = get_object_or_404(Pessoa, pk=pk)
    tokens = TokenUsuario.objects.filter(criado_por=pessoa, ativo=True, utilizado=False)
    for token in tokens:
        token.ativo = False
        token.save()

    novo_token = TokenUsuario()
    novo_token.criado_por = pessoa
    novo_token.chave = uuid.uuid4()
    novo_token.data_criacao = datetime.now()
    novo_token.data_validade = novo_token.data_criacao + timedelta(minutes=120)
    novo_token.utilizado = False
    novo_token.ativo = True
    novo_token.save()

    titulo = "Solicitação de troca de senha #%d" % novo_token.pk
    remetente_email = 'Totem IFRS'

    context = {}
    context['token'] = novo_token
    context['url_externa'] = settings.URL_EXTERNA

    conteudo_mensagem = get_template('tablet/email_token_template.html').render(context)
    destinatario_email = [remetente_email, pessoa.email]

    send_mail(
        titulo,
        conteudo_mensagem,
        remetente_email,
        destinatario_email,
        html_message=conteudo_mensagem,
        fail_silently=False)
    return Response({})


@api_view(['POST'])
@parser_classes((JSONParser,))
def get_senha_temporaria(request):
    senha = ''
    pk = request.data.get('pk')
    pessoa = get_object_or_404(Pessoa, pk=pk)
    letras = [l for l in string.ascii_lowercase]
    letras.remove('o')
    for i in range(3):
        senha = senha + str(random.choice(letras))
    for i in range(4):
        senha = senha + str(random.randint(1, 9))
    pessoa.senha_temporaria = senha
    tempo = datetime.now()
    pessoa.senha_validade = tempo + timedelta(minutes=10)
    pessoa.save()
    return Response({"senha_temporaria": pessoa.senha_temporaria})


def alterar_senha(request, chave_token):
    context = {}

    try:
        token_usuario = TokenUsuario.objects.get(chave=chave_token, ativo=True,
                                                 utilizado=False, data_validade__gte=datetime.now())
        context['criado_por'] = token_usuario.criado_por
        form = SenhaForm()
        context['form'] = form
        context['nome'] = token_usuario.criado_por.nome + " " + token_usuario.criado_por.sobrenome
        if request.method == 'POST':
            form = SenhaForm(request.POST)
            if form.is_valid():
                nova_senha = form.cleaned_data['senha']
                confirmacao_nova_senha = form.cleaned_data['confirmacao_senha']
                if nova_senha == confirmacao_nova_senha:
                    token_usuario.criado_por.senha = nova_senha
                    token_usuario.criado_por.save()
                    token_usuario.ativo = False
                    token_usuario.utilizado = True
                    token_usuario.data_utilizacao = datetime.now()
                    token_usuario.save()
                    context['senha_alterada'] = True
                    context['erro_confirmacao'] = False
                    return render(request, 'tablet/alterar_senha.html', context)
                else:
                    context['senha_alterada'] = False
                    context['erro_confirmacao'] = True
                    return render(request, 'tablet/alterar_senha.html', context)
    except ObjectDoesNotExist:
        context['erro_invalido'] = True

    return render(request, 'tablet/alterar_senha.html', context)
