class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde afuera.")
    
    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return "Soy un método accesible desde afuera."

# Crear una instancia de la clase
e = Ejemplo()

# Acceder al atributo público
print(e.atributo_publico())

# Llamar al método público
print(e.metodo_publico())