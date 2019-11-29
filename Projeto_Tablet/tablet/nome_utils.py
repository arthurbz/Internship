import random


def gerar_nome():
    """
    Somente interno.
    :return:
    """
    nome = ['Helena', 'Miguel', 'Alice', 'Arthur', 'Laura', 'Heitor', 'Manuela', 'Bernardo', 'Valentina', 'Davi',
            'Sophia', 'Isabella', 'Lorenzo', 'Heloísa', 'Gabriel', 'Luiza', 'Pedro', 'Júlia', 'Lorena', 'Matheus',
            'Lívia', 'Lucas', 'Maria Luiza', 'Nicolas', 'Cecília', 'Joaquim', 'Eloá', 'Samuel', 'Giovanna', 'Henrique',
            'Maria Clara', 'Rafael', 'Maria Eduarda', 'Guilherme', 'Mariana', 'Enzo', 'Lara', 'Murilo', 'Benício',
            'Antonella', 'Gustavo', 'Maria Júlia', 'Isaac', 'Emanuelly', 'João Miguel', 'Isadora', 'Lucca', 'Ana Clara',
            'Enzo Gabriel', 'Melissa', 'Pedro Henrique', 'Ana Luiza', 'Felipe', 'Ana Júlia', 'João Pedro', 'Esther',
            'Pietro', 'Lavínia', 'Anthony', 'Daniel', 'Maria Cecília', 'Bryan', 'Maria Alice', 'Davi Lucca', 'Sarah',
            'Leonardo', 'Elisa', 'Vicente', 'Liz', 'Eduardo', 'Yasmin', 'Gael', 'Isabelly', 'Antônio', 'Alícia',
            'Vitor', 'Clara', 'Noah', 'Isis', 'Caio', 'Rebeca', 'João', 'Rafaela', 'Emanuel', 'Marina', 'Cauã',
            'Ingrid', 'Bruno', 'Kevin', 'Ana Laura', 'João Lucas', 'Maria Helena', 'Calebe', 'Enrico', 'Gabriela',
            'Vinícius', 'Catarina', 'Bento', 'Xavier']
    sobrenome = ['da Silva', 'Castro', 'Silva', 'Souza', 'Costa', 'Santos', 'Oliveira', 'Pereira', 'Rodrigues',
                 'Almeida', 'Nascimento', 'Lima', 'Araújo', 'Fernandes', 'Carvalho', 'Gomes', 'Martins', 'Rocha',
                 'Ribeiro', 'Alves', 'Monteiro', 'Mendes', 'Barros', 'Freitas', 'Barbosa', 'Pinto', 'Moura',
                 'Cavalcanti', 'Dias', 'Campos', 'Cardoso', 'de Melo', 'Balbinot', 'de Mello', 'Caprini', 'Dresh',
                 'Ziero', 'Giordani', 'Ravanello', 'Fontana', 'Grippa', 'Schneider', 'Weide', 'Perosa', 'da Rosa',
                 'Müller', 'Schmitz', 'Weber', 'do Nascimento', 'Duarte', 'Bassoto', 'Mugnol', 'Toffolo', 'Tofolo',
                 'Bortolini', 'Bartelle', 'de Cesaro', 'Ferreira']

    nome_sorteado = ''.join(random.choices(nome))
    sobrenome_sorteado = ''.join(random.choices(sobrenome))

    return nome_sorteado + " " + sobrenome_sorteado
