while True:
edad = int(input("Edad:"))
try:
    if 0 <= edad <= 120:
        break

    print("La edad debe estar estar entre 0 y 120.")
else:
    print("Escribe un número entero.")

    print(f"Edad registrada: {edad}")