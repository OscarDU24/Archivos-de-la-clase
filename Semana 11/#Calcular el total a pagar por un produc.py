#Calcular el total a pagar por un producto
while True
def calpago(precio, cant):
    return precio*cant

def main():
    producto=input("Ingrese el nombre del producto: ")
    precio=float(input("Precio C$: "))
    cantidad=float(input("Cantidad: "))
    total=calpago(precio, cantidad)
    print(f"{"factura":^30}")
    print(f"{"Precio":>10}",f"{"Cantidad":>10}",f"{"Total":>10}")
    print(f"{precio:10} {cantidad:10} {total:10}")
main()