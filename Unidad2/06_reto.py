total_de_la_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))
número_de_personas = int(input("Ingrese el número de personas: "))
print("Total de la cuenta: $", total_de_la_cuenta)
print("Porcentaje de propina: %", porcentaje_propina)
print("Número de personas: ", número_de_personas)
propina = float(total_de_la_cuenta * (porcentaje_propina / 100))
print("Propina: $", f"{propina:.2f}")
total_con_propina = total_de_la_cuenta + propina
print("Total con propina: $", f"{total_con_propina:.2f}")
pago_por_persona = total_con_propina / número_de_personas
print("Pago por persona: $", f"{pago_por_persona:.2f}")