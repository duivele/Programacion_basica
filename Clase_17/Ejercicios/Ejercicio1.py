class Pelicula:
    # Constructor de clase
    def _init_(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f'Se ha creado la película: {self.titulo}')

    # Método _str_ para representar la película como string
    def _str_(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)

class Catalogo:

    # Atributo para almacenar las películas
    def _init_(self, peliculas=None):
        if peliculas is None:
            peliculas = []
        self.peliculas = peliculas

    # Método para agregar una película al catálogo
    def agregar(self, p):
        self.peliculas.append(p)

    # Método para mostrar todas las películas en el catálogo
    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)

# Crear instancias de Pelicula
p = Pelicula("El padrino", 175, 1972)

# Crear una instancia de Catalogo y agregar la película
c = Catalogo([p])  # Añadir una lista con una película desde el principio
c.mostrar()

# Añadir otra película al catálogo
c.agregar(Pelicula("El padrino parte 2", 202, 1974))
c.mostrar()