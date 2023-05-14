#1. pedirle al usuario que introduzca
#cantidad de horas y valor por hora
#2. cuando horas lleguen hasta 40 se paga a 10.5
#3. cuando horas sobrepasan 40 se pagan 1.5 veces más caras
#4. Crear una función llamada "computepay()"
#5. esa función debe retornar un valor (498.75)

def computepay(h,r):
    h = float(input("Ingrese horas:"))
    r = float(input("Ingrese valor x hora:"))

    if h <= 40:
        producto = h * r
        return producto
    else:
        producto = ((h - 40) * r *1.5) + (40 * r)
        return producto

print(computepay(5, 1.5))
