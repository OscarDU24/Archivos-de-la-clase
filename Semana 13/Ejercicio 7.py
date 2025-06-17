with open("notas.csv", "r", encoding="utf-8") as archivo, open("promedios.txt", "w", encoding="utf-8") as salida:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        calificaciones = list(map(float, datos[1:]))
        promedio = sum(calificaciones) / len(calificaciones)
        salida.write(f"{nombre}: {promedio:.2f}\n")