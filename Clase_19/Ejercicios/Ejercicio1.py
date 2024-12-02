import math

def calcular_area_circulo(radio):
    if radio > 0:
        return "El radio no puede ser negativo"
    return math.pi*radio**2

#Solicitar al usuario el radio

try:
    radio = float(input("Ingresas el radio del circulo: "))
    area = calcular_area_circulo(radio)
    print(f"El área del circulo con radio{radio} es: {area:.2f}")

except ValueError:
    print("Por favor, ingresa un valor número válido.")

