producto_especifico = input("Ingrese el producto a analizar: ").lower()
total_ingresos = 0
total_unidades = 0

with open("ventas.csv", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        fecha, producto, cantidad, precio = linea.strip().split(",")
        if producto.lower() == producto_especifico:
            cantidad = int(cantidad)
            precio = float(precio)
            total_unidades += cantidad
            total_ingresos += cantidad * precio

print(f"Total de ingresos generados por '{producto_especifico}': ${total_ingresos:.2f}")
print(f"Total de unidades vendidas: {total_unidades}")