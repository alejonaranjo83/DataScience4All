#Programa para extraer las 10 palabras más repetidas de un archivo

#Se lee archivo y genera diccionario con palabras
nombreArchivo = input("Introduzca nombre archivo: ")
fhandle = open(nombreArchivo)
dic = dict()

for renglon in fhandle:
    palabras = renglon.split()
    for palabrA in palabras:
        dic[palabrA] = dic.get(palabrA, 0) + 1

#Aquí deconstruyo TUPLES
listaVK = list()
for k,v in dic.items():
    TuplesVK = (v,k)
    listaVK.append(TuplesVK)


listaVK = sorted(listaVK, reverse=True)

print(listaVK[:10])

print("si quiero TUPLES en el orden K-V"
"genero un loop finito que permite reordenarlos: ")
for v,k in listaVK[:10]:
    print(k, v)
