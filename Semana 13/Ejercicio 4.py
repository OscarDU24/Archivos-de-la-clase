with open("original.txt", "r", encoding="utf-8") as origen, open("copia.txt", "w", encoding="utf-8") as destino:
    destino.write(origen.read())