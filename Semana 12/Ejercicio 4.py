# Paso 1: Abrir el archivo en modo lectura
with open("productos.csv", "r", encoding="utf-8") as archivo:
    # Paso 2: Recorrer el archivo línea por línea
    for linea in archivo:
        # Paso 3: Eliminar el salto de línea final
        linea = linea.strip()
        # Paso 4: Separar por comas
        nombre, precio, cantidad = linea.split(",")
        # Paso 5: Mostrar la información de forma legible
        print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")
# El archivo se cierra automáticamente con 'with'