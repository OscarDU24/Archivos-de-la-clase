archivo = "documento.txt"
palabra_original = input("Palabra a buscar: ")
palabra_nueva = input("Palabra nueva: ")

with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read().replace(palabra_original, palabra_nueva)

with open("modificado.txt", "w", encoding="utf-8") as f:
    f.write(contenido)

print("Reemplazo completado.")