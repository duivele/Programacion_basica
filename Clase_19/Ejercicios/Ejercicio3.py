from datetime import datetime

#fecha y hora actual

ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")

#Entrada de usuario

fecha_str = input("Ingrese una fecha pasada(YYYY-mm_DD): ")
fecha_past = datetime.strptime(fecha_str,"%Y-%m-%d")

#Calculo de dias transcurridos

diferencia = ahora - fecha_past
print(f"Dias transcurridos desde {fecha_past.date()}: {diferencia.days} dias")