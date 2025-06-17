archivo = "articulo.txt"
palabra = input("Ingrese la palabra a contar: ").lower()
contador = 0

with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        contador += linea.lower().split().count(palabra)

print(f"La palabra '{palabra}' aparece {contador} veces.")