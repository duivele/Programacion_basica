import math

numero = float(input("Ingresa un número: "))

raiz = math.sqrt(numero)
seno = math.sin(math.radians(numero))
coseno = math.cos(math.radians(numero))

print(f"La raiz del número es: {raiz}")
print(f"El seno del número es: {seno}")
print(f"El coseno del número es: {coseno}")

if numero.is_integer() and numero >= 0:
    factorial = math.factorial(int(numero))
    print(f"Factorial: {factorial}")
else: 
    print("No se puede calcular el factorial del número")