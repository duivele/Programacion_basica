#Define la cantidad de puntos de tu linea
length = int (input("Ingrese la longitud de la línea de puntos: "))
direction = input ("Horizontal (h) o Vertical (v): ").lower()
if direction == "h":
    print("*")
elif direction == "v":
    for _ in range (length): 
        print("*")
else:
    print("Dirección no válida")