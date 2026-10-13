import math

def cuadrado(lado):
    area = lado**2
    return(area)

def triangulo(base, altura):
    area = (base * altura) / 2
    return(area)

def circulo(radio):
    area = (math.pi * radio**2)
    return(area)