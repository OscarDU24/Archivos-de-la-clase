# Paso 1: Abrimos el archivo en modo escritura para iniciar una nueva lista
with open("compras.txt", "w", encoding="utf-8") as archivo:
    # Paso 2: Bucle infinito
    while True:
        # Paso 3: Pedir al usuario un producto
        producto = input("Ingresa un producto (o escribe 'fin' para terminar): ")

        # Paso 4: Verificar si la entrada es 'fin' para terminar
        if producto.lower() == "fin":
            break
        
        # Paso 5: Escribir el producto en el archivo
        archivo.write(producto + "\n")

# Paso 6: Notificar al usuario que la lista fue guardada
print("¡Tu lista de compras ha sido guardada en 'compras.txt'!")
