with open("notas.txt", "w", encoding="utf-8") as archivo:
    while True:
        linea = input("Ingrese una línea de texto (o 'FIN' para terminar): ")
        if linea.upper() == "FIN":
            break
        archivo.write(linea + "\n")