n = int(input("Ingrese un número:"))

# 1. Evaluar si es Primo
es_primo = True

if n <= 1:
    es_primo = False
else:
    i = 2
    while i < n:
        if n % i == 0:
            es_primo = False
            break
        i += 1

if es_primo:
    print("es primo")
else:
    print("no es primo")
a = 0
b = 1
if a < n:
    siguiente = a + b
    a = b
    b = siguiente
while a < n:
    a == n
if a == n:
    print("Esta en Fibonacci")
else:
    print("No esta en Fibonacci")