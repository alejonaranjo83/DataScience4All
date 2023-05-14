#Inserte cantidad de horas
hrs = input("Enter Hours:")
#convierta ese "string" en un decimal "float"
h = float(hrs)
#Indique a cuánto se paga la hora hasta 40h
rate_below40 = input("Enter Rate below 40")
#convierta ese valor en decimal
rateBe40 = float(rate_below40)
#indique a cuánto se paga la hora por encima de 40h
rate_above40 = input("Enter Rate above 40")
#convierta ese valor en decimal
rateAb40 = float(rate_above40)

#haga esto si la cantidad de horas está por debajo de 40h
if(h <= 40):
    pagar = rateBe40 * h
    print(pagar)
#de lo contrario, haga esto
else:
    pagarEncima40 = (h - 40) * rateAb40
    pagarHasta40 = 40 * rateBe40
    pagoCompleto = pagarEncima40 + pagarHasta40
    print(pagoCompleto)





#Esto hace lo mismo que lo de arriba, pero
#no le pide al usuario que indique el valor
#por hora, solamente la cantidad de horas

hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.50

if(h <= 40):
    pagar = rate * h
    print(pagar)
else:
    pagarEncima40 = (h - 40) * (rate * 1.5)
    pagarHasta40 = 40 * rate
    pagoCompleto = pagarEncima40 + pagarHasta40
    print(pagoCompleto)

print(type(pagoCompleto))
