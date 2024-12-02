def main(): 1usage

    while True:
        try:
        N = int(input("Ingrese el número de alumnos: "))
        if N <= 0:
            print("El número de alumnos debe ser mayor que 0. ")
            continue
        break
        except ValueError:
        print("Por favor, ingrese un número entero válido. ")
        
    for i in range(N):
        print(f"\nAlumno {i + 1}: ")
        nombre = input ("Ingrese el nombre del alumno: ").strip()
        cursos = []
        for j in range(m):
        curso = input(f"Ingrese el nombre del curso {j + 1}: ").strip()
        cursos.append(curso)
        alumnos.append({
        'nombre' : nombre,
        'cursos' : cursos,
        
        })           
        print("\nInformación de los alumnos: ")
        for alumno in alumnos:
        print(f"\nNombre: {alumno['nombre']}")
        print("Cursos:")
        for curso in alumno['cursos']:
        print(f"- {curso}")
        
        while True:
        try:
        m = int(input("Ingrese la cantidad de cursos que está tomando: "))
        if m < 0:
         print("La cantidad de cursos no puede ser negativa.")
        continue
        break
        except ValueError:
        print("Por favor, ingrese un número entero válido.")