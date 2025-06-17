#Generador de recibos de diferentes productos
def calcpago(precio, cant):
    return precio*cant

def main():
    productos=[]
    precios=[]
    cantidades=[]
    totales=[]
    resp= "SI"
    while resp.upper() != "NO":
        producto=input("Nombre del producto: ")
        precio=float(input("Precios: "))
        cantidad=float(input("Cantidad: "))
        total= calcpago(precio, cantidad)

        productos.append(producto)
        precios.append(precio)
        cantidades.append(cantidad)
        totales.append(total)

        print("Desea agregar otro producto Si - No")
        resp=input("Respuesta ")

        print(f"{"Factura":^30}")
        print(f"{"Producto":<10}",F"{"Precio":>10}",f"{"Cantidad":>10}",f"{"Total":>10}")
        tam=len(productos)
        for i in range(tam):
            print(f"{productos[i]:<10} {precios[i]:10} {cantidades[i]:10} {totales[i]:10}")

        monto=sum(totales)
        print("Total a pagar C$: ",monto)
main()