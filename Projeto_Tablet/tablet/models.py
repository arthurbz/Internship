from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, unique=True)
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=20)
    senha_temporaria = models.CharField(max_length=20, null=True, blank=True)
    senha_validade = models.DateTimeField(null=True, blank=True)
    email = models.CharField(max_length=40)

    class Meta:
        unique_together: ['cpf', 'matricula']


class TokenUsuario(models.Model):
    chave = models.CharField(max_length=36)
    data_validade = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_utilizacao = models.DateTimeField(null=True, blank=True)
    utilizado = models.BooleanField(False)
    ativo = models.BooleanField(True)
    criado_por = models.ForeignKey(Pessoa, related_name='tokens_criados', on_delete=models.CASCADE)
