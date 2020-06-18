import math    # Biblioteca math para calculos
from fractions import Fraction    # Bilioteca fractions para fração


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


def grausRadFracao(grau):
    """
    Transforma o angulo em graus para radianos em forma de fração com o
    simbolo π
    :param valora: Valor em graus
    :return: Fração com o valor de π
    """
    divisao = str(Fraction(grau) / Fraction(180, 1))
    if divisao.count("/") < 1:
        if divisao == "1":
            return "𝜋"
        else:
            return divisao + "𝜋"
    else:
        if divisao[:divisao.find("/")] == "1":
            return "𝜋" + divisao[divisao.find("/"):]
        else:
            return divisao[:divisao.find("/")] + "𝜋" + divisao[divisao.find("/"):]


# inicio do programa
layout("FUNÇÕES TRIGONOMÉTRICAS")
angulo = float(input("  >> DIGITE O VALOR DO ÂNGULO: "))

seno = math.sin(convGrausRad(angulo))    # Calculando seno
cos = math.cos(convGrausRad(angulo))    # Calculando cosseno
tan = math.tan(convGrausRad(angulo))    # Calulando tangente
rad = convGrausRad(12)    # Transformando graus para radianos

print()
layout("RESULTADOS")
print(f' > Para o angulo {angulo}:\n    Seno = {seno:.2f}\n    Cosseno = '
      f'{cos:.2f}\n    Tangente = {tan:.2f}\n    Radianos = '
      f'{convGrausRad(angulo):.2f} ou {grausRadFracao(angulo)}')

