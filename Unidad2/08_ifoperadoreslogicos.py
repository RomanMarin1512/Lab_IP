edad = 15 # años
tiene_credencial = True # tiene credencial
tiene_adeudo = False # no tiene adeudo
if edad >= 18: # es mayor de edad
    es_mayor = True
else:
    es_mayor = False
if tiene_credencial: # tiene credencial
    documento_valido = True
else:
    documento_valido = False
if not tiene_adeudo: # no tiene adeudo
    sin_adeudo = True
else:
    sin_adeudo = False
autorizado = es_mayor and documento_valido and sin_adeudo
print(autorizado)