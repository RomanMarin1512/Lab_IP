numero, hexadecimal = "0", "" # Número a convertir y resultado en hexadecimal
if numero == "0": print ("0") # Si el número es 0, imprimimos 0
digitos = "0123456789ABCDEF" # lista de dígitos hexadecimales
while numero > "0": hexadecimal, numero = digitos[numero % 16] + hexadecimal, numero // 16 #mientras el número sea mayor que 0, calcular el residuo de la división entre 16 y lo agregamos al inicio de la variable hexadecimal, luego dividimos el número entre 16 y lo guardamos en la variable numero
print(hexadecimal) #Imprimimos el número hexadecimal