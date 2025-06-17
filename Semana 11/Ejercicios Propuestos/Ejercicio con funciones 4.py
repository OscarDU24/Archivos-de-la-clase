#Programa para grabar el número de horas trabajadas
def calcular_pago(horas):
    if horas <= 160:
        pago = horas * 6.5
    else:
        pago = (160 * 6.5) + ((horas - 160) * 7.5)
    return pago

horas = int(input("Ingrese el número de horas trabajadas: "))
total_pago = calcular_pago(horas)
print("Total a pagar por horas trabajadas:", total_pago)