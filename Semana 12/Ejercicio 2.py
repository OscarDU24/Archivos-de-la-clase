# Paso 1: Pedir al usuario el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo (por ejemplo, poema.txt): ")

# Paso 2: Usar try...except para manejar errores
try:
    # Paso 3: Abrir el archivo en modo lectura
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        # Paso 4: Leer todas las líneas
        lineas = archivo.readlines()
        # Paso 5: Calcular y mostrar la cantidad de líneas
        print(f"El archivo tiene {len(lineas)} líneas.")
except FileNotFoundError:
    # Paso 6: Manejo del error si el archivo no existe
    print("Error: El archivo no fue encontrado. Asegúrate de que el nombre sea correcto.")