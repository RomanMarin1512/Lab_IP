numero, octal = 8, "" # Guardamos la varaible en la que se encuentra el número a convertir y creamos una variable vacía para almacenar el número octal
if numero == 0: print (0) # Si el número es 0, imprimimos 0
while numero > 0: octal, numero = str(numero % 8) + octal, numero // 8 # Mientras el número sea mayor que 0, calculamos el residuo de la división entre 8 y lo agregamos al inicio de la variable octal, luego dividimos el número entre 8 y lo guardamos en la variable numero
print(octal) # Imprimimos el número octal