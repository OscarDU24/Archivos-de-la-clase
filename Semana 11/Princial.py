#Programa principal

import Modulos as md

#otra forma de importar modulos
from Modulos import texto

print("Calcula las operaciones basicas con modulo")
n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
print(f"EL producto de los números es: {md.producto(n1,n2)}")
resp=md.restar(n1,n2)
print("La resta es:",resp)
print(texto)
print("La suma es:",md.suma(n1,n2))
print("La resta es:",resp)
print("La division es:",md.division(n1,n2))