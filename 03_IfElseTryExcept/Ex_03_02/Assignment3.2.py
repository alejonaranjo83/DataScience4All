hrs = input("Enter Hours:")
rate_below40 = input("Enter Rate below 40")
rate_above40 = input("Enter Rate above 40")

#Como sé que el usuario puede ingresar valor en letras
#uso las funciones "try" y "except"
#en el bloque de "try" hago las cosas como espero que
#el usuario las haga:
try:
    h = float(hrs)
    rateBe40 = float(rate_below40)
    rateAb40 = float(rate_above40)
#En el bloque de "except" genero alerta para que el
#usuario sepa qué es lo que no funcionó
except:
    print("Error: por favor digite valor numerico")
    #la función "quit" aparece para facilitar la lectura
    #del error y que solo se vea este primer error. De lo
    #contrario, el código se sigue ejecutando y saca otro error
    quit()

if(h <= 40):
    pagar = rateBe40 * h
    print(pagar)
else:
    pagarEncima40 = (h - 40) * rateAb40
    pagarHasta40 = 40 * rateBe40
    pagoCompleto = pagarEncima40 + pagarHasta40
    print(pagoCompleto)
