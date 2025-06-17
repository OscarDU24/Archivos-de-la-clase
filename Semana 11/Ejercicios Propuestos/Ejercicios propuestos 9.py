#Ejercicios propuestos 9
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número entero para su tabla de multiplicar: "))
tabla_multiplicar(num)