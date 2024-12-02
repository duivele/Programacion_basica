N = int(input("Ingresar cantidad de estudiantes: "))
i = 1

while N >= i:
    nombre = input("ALUMNO {}: ".format(i))
    
    M = int(input("Ingresar cantidad de cursos: "))
    j = 0 
    while M > j:
        curso_nombre = input("CURSO {}: ".format(j + 1))
        j += 1  
        
    i += 1  
