def suma(a,b):
    return a+b
def resta(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a,b):
    if b !=0:
        return a / b
    else:
        return "no se puede dividir por cero"
def calculadora():
    print("Elige una operación: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = int(input("Eliga una opcion (1/2/3/4): "))
    num1 = float(input("Escribe el primer numero: "))
    num2 = float(input("Escribe el segundo numero: "))       
    
    if opcion==1:
        print(suma(num1, num2))
    elif opcion==2:
        print(resta(num1, num2))
    elif opcion==3:
        print(multiplicar(num1, num2))
    elif opcion==4:
        print(dividir(num1, num2))

calculadora()