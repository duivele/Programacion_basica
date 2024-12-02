import csv
import random

nombres = ["Juan", "Ana", "Luis", "Sofia"]
edades = [20, 21, 22, 23]
notas = [4.5, 5.0, 6.0, 7.0]

with open("estudiantes.csv", mode="w", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(["Nombre", "Edad", "Notas"])
    
    for _ in range(10):
        nombre = random.choice(nombres)
        edad = random.choice(edades)
        nota = random.choice(notas)
        escritor.writerow([nombre, edad, nota])
    
print("Archivo CSV generado correctamente")