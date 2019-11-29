import random

def gerar_cpf():
    """
    Somente interno.
    :return:
    """
    numeros = []
    for i in range(11):
        numeros.append(random.randint(0, 9))
    numeros_str = [str(n) for n in numeros]

    return ''.join(numeros_str)