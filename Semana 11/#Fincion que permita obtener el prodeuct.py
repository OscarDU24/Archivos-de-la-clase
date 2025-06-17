#Fincion que permita obtener el prodeucto de 2#
def producto(num1,num2):
    return num1*num2
#Multiplicar 2 #
numero1=int(input("Digite #: "))
numero2=int(input("Digite otro #: "))
resp=producto(numero1,numero2)
print(numero1, " * ", numero2, " = ",resp)

#Obtener al tabla de multiplicar de un #
num=int(input("Escriba un # "))
for i in range(1, 13):
    r=producto(num,i)
    print(num, " * ",i, " = ",r)
