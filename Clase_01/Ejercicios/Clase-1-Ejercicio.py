#Definir la lista de ganadores con su nombre, edad y género
ganadores = [
    {"nombre": "Juan", "edad": 25, "genero": "hombre"},
    {"nombre": "María", "edad": 20, "genero": "mujer"},
    {"nombre": "Pedro", "edad": 19, "genero": "hombre"},
    
]

#Función para verificar si un ganador puede entrar al boliche

def puede_entrar(ganador):
    if ganador ["genero"]== "hombre":
        return ganador["edad"] > 21
    elif ganador ["genero"] == "mujer":
        return ganador["edad"] > 18
    else:
        return False

#Verificar cada ganador y determinar quiénes pueden entrar al boliche
for ganador in ganadores:
    if puede_entrar(ganador):
        print(f"{ganador} ['nombre'] puede entrar al boliche.")
    else:
        print(f"{ganador['nombre']} no puede entrar al boliche.")