import matplotlib.pyplot as plt

#PARA USAR ESTA LIBRERIA HAY QUE INSTALAR PIP INSTALL matplotlib

def graficar_ventas(categorias,ventas):
    plt.bar(categorias, ventas, color = 'skyblue')
    plt.xlabel('Categorías')
    plt.ylabel('Ventas')
    plt.title('Ventas por categorías')
    plt.show()

categorias = ['Electrónica', 'ropa', 'Alimentos', 'Libros']
ventas = [150,200,120,90]

graficar_ventas(categorias, ventas)