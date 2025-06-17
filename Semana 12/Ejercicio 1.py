import datetime

# Paso 2: Pedir al usuario una entrada para el diario
entrada = input("Escribe tu entrada para el diario: ")

# Paso 1: Obtener la fecha y hora actual
fechahoraactual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Paso 3: Abrir el archivo en modo de adición ('a')
with open("diario.txt", "a", encoding="utf-8") as archivo:
    # Paso 4: Escribir la fecha, hora y la entrada del usuario
    archivo.write(f"{fechahoraactual} - {entrada}\n")

# Paso 6: Mostrar mensaje de confirmación
print("Tu entrada ha sido guardada exitosamente en el diario.")