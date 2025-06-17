#Ejercicios propuestos 8
def calcular_descuento(compra):
    if compra > 500:
        descuento = compra * 0.12
    elif compra > 300:
        descuento = compra * 0.10
    else:
        descuento = compra * 0.05
    return compra - descuento

importe = float(input("Ingrese el importe de la compra: "))
importe_final = calcular_descuento(importe)
print("Importe final a pagar:", importe_final)