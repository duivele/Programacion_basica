def calcularNota (n1,n2,n3):
    return (n1*0.3 + n2*0.3 + n3*0.4)

n1=float(input("ingrese la primera nota: "))
n2=float(input("ingrese la segunda nota: "))
n3=float(input("Ingrese la tercera nota: "))

notaFinal=calcularNota(n1, n2, n3)

print("La nota final del estudiante es: ", notaFinal)