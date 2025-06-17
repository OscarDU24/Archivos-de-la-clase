from datetime import datetime

evento = input("Ingrese el evento a registrar: ")
hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{hora_actual} - {evento}\n")

print("Evento registrado.")