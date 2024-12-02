#Lista de invitados
invitados = ["Juan", "María", "Pedro", "Ana", "Luis"]

#Nombre de la persona que intenta entrar
persona = "María"

#Verificar si la persona está en la lista de invitados
if persona in invitados:
    print(f"{persona} está en la lista de invitados. Puede entrar.")
else:
    print(f"{persona} no está en la lista de invitados. No puede entrar.")
