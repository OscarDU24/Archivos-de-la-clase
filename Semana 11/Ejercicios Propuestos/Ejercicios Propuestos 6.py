#Ejercicios Propuestos 6
import math

def area_circulo(radio):
    return math.pi * radio ** 2

radio = float(input("Ingrese el radio del círculo: "))
resultado = area_circulo(radio)
print("Área del círculo:", resultado)