import math


def convGrausRad(valor: float):  # Graus para Radianos
    """
    Transforma um valor em graus para um valor em radiano
    :param valor: Valor em graus
    :return: Valor em radianos
    """
    rad = (valor / 180) * math.pi
    return rad


def layout(texto: str):
    """
    Desenha o layout do cabeçalho
    :param texto: String contendo o texto
    """
    print("|" + "=" * 35 + "|")
    print("|" + texto.center(35) + "|")
    print("|" + "=" * 35 + "|\n")


# inicio do programa
layout("FUNÇÕES TRIGONOMÉTRICAS")
angulo = float(input("  >> DIGITE O VALOR DO ÂNGULO: "))

seno = math.sin(convGrausRad(angulo))    # Calculando seno
cos = math.cos(convGrausRad(angulo))    # Calculando cosseno
rad = convGrausRad(12)    # Transformando graus para radianos

print()
layout("RESULTADOS")
print(f' > Para o angulo {angulo}:\n    Seno = {seno:.2f}\n    Cosseno = {cos:.2f}\n     Radianos = {convGrausRad(angulo):.2f}')


