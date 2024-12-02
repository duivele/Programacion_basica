class Empleado:
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    # Método para calcular el salario mensual
    def calcular_salario_anual(self):
        return self.salario_mensual * 12
    
    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, salario mensual: {self.salario_mensual}")
    
empleado1 = Empleado("Ana", 2000)

empleado1.mostrar_informacion()
print(f"Salario anual: {empleado1.calcular_salario_anual()}")   