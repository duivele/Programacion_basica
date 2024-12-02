#Haz un “collage de símbolos”
#Descripción: Genera un collage de símbolos de manera aleatoria en una cuadrícula de 10x10, 
#usando varios caracteres diferentes (como “#”, “*”, “@”). 
#Cada posición de la cuadrícula debería mostrar un símbolo aleatorio.
#Conceptos: Uso de listas, biblioteca random.
import random
symbols = ["#""*""@""&"]
for y in range(10):
    line = " "
    for x in range (10):
        line += random.choice (symbols) + " "
print(line)