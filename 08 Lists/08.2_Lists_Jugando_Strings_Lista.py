# 1. Con el comando .split puedo convertir "string´s" en listas:
print("Esta es una string:")
Nombre = "Alejandro Antonio Naranjo Gaviria"
print(Nombre, type(Nombre))
print("que se puede transformar en una lista con fxn .split()")
NombreEnLista = Nombre.split()
print(NombreEnLista)
print("Al tenerlo en una lista, es más fácil extraer elementos, sin tener que contar posición caracteres:")
print("Aquí por ejemplo extraigo el 2do elemento:", NombreEnLista[1])

print(" ")

# 2. Con la función .split se facilita la extracción de elementos
# de un archivo tipo "email"

print("A continuación se extraerán los días de un archivo de mails")
print("para lo cual se creará una lista con las líneas que interesan")
print("y de esas líneas se extraerán los elementos correspondientes al día")

fhandle = open("mbox-short.txt")
count = 0

for lineas in fhandle:
    lineas = lineas.rstrip()
    if not lineas.startswith("From "):
        continue
    ListaPalabras = lineas.split()
    print(ListaPalabras[2])
    if lineas.startswith("From "):
        count = count + 1
print ("El archivo contiene", count, "líneas que inician con From e indican el día")
print(" ")

# 3. Lo que se ponga en el paréntesis de la fxn .split
# será el criterio q utiliza python para identificar/descomponer
# las piezas que compondrán la lista

print ("A continuación se hará una lista a partir de otra lista")
print ("y de esta manera se extraerán los lugares")
print ("de donde viene cada correo con más facilidad")
print ("y posibilidad de control:")

fhandle = open("mbox-short.txt")

for lineas in fhandle:
    lineas = lineas.rstrip()
    if not lineas.startswith("From "):
        continue
    ListaPalabras = lineas.split()
    email = ListaPalabras[1]
    DeDonde = email.split("@")
    print(DeDonde[1])
