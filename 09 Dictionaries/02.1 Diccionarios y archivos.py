# Ejemplo 1:
#Se abre archivo:
nombreArchivo = input("Introduzca nombre archivo: ")
portal = open(nombreArchivo)

#Se genera un loop dentro de otro loop para dividir texto
#en renglones y posteriormente en las palabras de cada renglon
#Una vez hecho esto, se crea diccionario con palabras que no
#estén previamente dentro del mismo y se contabiliza
#cuántas veces aparece cada una:
cuenta = dict()
for renglon in portal:
    renglon = renglon.split()
    for palabras in renglon:
        cuenta[palabras] = cuenta.get(palabras, 0) + 1
print("Hasta aquí se obtienen las palabras con sus respectivas")
print("repeticiones, pero estas no están en orden:")
print(cuenta)
print(" ")

#Hecho lo anterior se procede a identificar cuál es la palabra
#q más se repite y la cantidad de veces que se repite
RepeticMax = None
PalabraMasRepet = None
#sobre variables previamente creadas que se irán modificando
#conforme aparezca una palabra que se repita más veces,
#estas irán variando
for palabra,repetic in cuenta.items():
#se crean dos variables que iteren al mismo tiempo
#sobre el diccionario creado anteriormente; la primera
#de ellas itera sobre las KEYS y la otra sobre VALUES
    if RepeticMax is None or repetic > RepeticMax:
    #Si RepeticMax es el primer valor...
    #O si la repetición actual es mayor q la q había
    #previamente
        #Entonces recuerde dicha variable... la palabra
        #q más se repitió con la respectiva cantidad
        #de veces q se repite
        RepeticMax = repetic
        PalabraMasRepet = palabra

print("Esta es la palabra más repetida con su respectiva cantidad de veces q se repite")
print(PalabraMasRepet, RepeticMax)
