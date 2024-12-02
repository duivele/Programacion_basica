class Coche:
    # Definir la clase coche
    # El método __init__ es el constructor, se llama para crear un objeto
    def __init__(self, marca, modelo, color):  # Corregido a __init__
        self.marca = marca  # Atributo de marca
        self.modelo = modelo  # Atributo de modelo
        self.color = color  # Atributo de color
        self.en_marcha = False  # Atributo para saber si el coche está en marcha

    # Método para arrancar el coche
    def arrancar(self):
        if not self.en_marcha:
            self.en_marcha = True  # Corregido a True
            print(f"El coche {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está en marcha.")

    # Método para detener el coche
    def detener(self):
        if self.en_marcha:
            self.en_marcha = False  # Corregido a False
            print(f"El coche {self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está detenido.")

    # Método para mostrar el estado del coche
    def mostrar_estado(self):
        estado = "en marcha" if self.en_marcha else "detenido"
        print(f"El coche {self.marca} {self.modelo}, color: {self.color}, está {estado}.")

# Crear objetos (instancias) de la clase coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")
tu_coche = Coche("Honda", "Civic", "Azul")

# Mostrar el estado de los coches
mi_coche.mostrar_estado()
tu_coche.mostrar_estado()

# Arrancar los coches
mi_coche.arrancar()
tu_coche.arrancar()

# Detener los coches
mi_coche.detener()
tu_coche.detener()

# Mostrar el estado final de los coches
mi_coche.mostrar_estado()
tu_coche.mostrar_estado()
