#Escribir un programa que permita ingresar los salarios de una cantidad indicada de empleados

#Crear la función
def calculardescuento(salario):
    return salario * 0.10

#Solicitar la cantidad de empleados
nempleados = int(input("Ingrese la cantidad de empleados: "))
totalpagos = 0
totaldescuentos = 0

#Calcular el descuento y el total a pagar
for i in range(nempleados):
    salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
    descuento = calculardescuento(salario)
    totalempleado = salario - descuento
    
    print(f"Empleado {i+1}:")
    print(f"Salario bruto: ${salario:.2f}")
    print(f"Descuento (10%): ${descuento:.2f}")
    print(f"Total a pagar: ${totalempleado:.2f}")
    print()