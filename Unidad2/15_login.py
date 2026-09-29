MAX = 3
for intento in range (1, MAX + 1):
    usuario = input ("Usuario: ")
    clave = input ("Clave: ")

    if usuario == "alumno" and clave == "Chagotactico123":
        print("Bienvenido")
        break

    print("Credenciales incorrectas")
else:
    print("Acceso bloqueado")
    