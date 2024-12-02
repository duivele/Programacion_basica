
#usuario predefinido
username = "admin"
password =  "1234"
intentos = 3
while intentos > 0:
    user_input = input("Introduce el nombre de usuario: ")
    pass_input = input("Introduce la contraseña: ")
    
    if user_input == username and pass_input == password:
        print("Autenticación exitosa")
        break
    
    else: 
        intentos -= 1
        print(f"Intentos restantes: {intentos}")
else: 
    print("Cuenta bloqueada")
    