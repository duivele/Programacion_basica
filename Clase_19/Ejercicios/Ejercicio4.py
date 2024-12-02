import turtle

def dibujar_casa():
    pantalla = turtle.Screen()
    pantalla.title("Dibujo de una casa")
    
    lapiz = turtle.Turtle()
    lapiz.speed(2)
    
    # Dibujar la base
    for _ in range(4):
        lapiz.forward(100)
        lapiz.left(90)
    # dibujar el techo
    
    
    lapiz.left(45)
    lapiz.forward(70)
    lapiz.right(90)
    lapiz.forward(70)
    lapiz.right(135)
    lapiz.forward(100)
    
    pantalla.mainloop()

dibujar_casa()