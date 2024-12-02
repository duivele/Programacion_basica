waves = int (input("Ingrese un número: "))
for _ in range(3):  # Número de líneas de ondas.
    for _ in range(waves):
        print("~ ", end="")  # Imprime la primera fila de ondas.
    print()  # Salto de línea.
    for _ in range(waves):
        print(" ~", end="")  # Imprime la segunda fila de ondas desplazada.
    print()  # Salto de línea.