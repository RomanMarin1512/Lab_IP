numero = 11 
if numero == 0:
        print ("0")
Hexadecimal = ""
while numero > 0:
    residuo = numero % 16
    if residuo < 10:
        Hexadecimal = str(residuo) + Hexadecimal
    else:
        Hexadecimal = chr(residuo + 55) + Hexadecimal
    numero = numero // 16
print(Hexadecimal)