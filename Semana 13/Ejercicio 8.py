palabra = input("Ingrese la palabra clave: ").lower()

with open("libro.txt", "r", encoding="utf-8") as entrada, open("filtrado.txt", "w", encoding="utf-8") as salida:
    for linea in entrada:
        if palabra in linea.lower():
            salida.write(linea)