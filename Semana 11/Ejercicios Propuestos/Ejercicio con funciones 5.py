#Ejercicios propuestos 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(num)
print(f"Factorial de {num} es {resultado}")