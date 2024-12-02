def verificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

resultado = verificar_numero(0)
print(f"El numero 3 es {resultado}")
