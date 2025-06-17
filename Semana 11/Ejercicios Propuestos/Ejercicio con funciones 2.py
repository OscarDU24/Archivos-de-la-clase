#Función para calcular a comisión

#Formar la funsion 
def calcularcomisiones(ventas):
    return ventas * 0.10

#Solicitar los vendedores y el sueldo
nvendedores = int(input("Ingrese el número de vendedores: "))
sueldobase = float(input("Ingrese el sueldo base: "))

#Solicitar el monto total de las 3 ventas por vendedor
for i in range(nvendedores):
    ventas = float(input(f"Ingrese el monto total de las 3 ventas del vendedor {i+1}: "))
    comision = calcularcomisiones(ventas)
    total = sueldobase + comision
    
    print(f"Vendedor {i+1}:")
    print(f"Comisiones: ${comision:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print()