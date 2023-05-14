nombre = "alejandro"
letras = nombre[3]
print (letras)

#Hace lo mismo de arriba con menos código
nombre = "alejandro"
print (nombre[3])

#Para saber cuántos elementos tiene una función
#la longitud (como en R)
nombre = "alejandro"
print (len(nombre))

#Para saber cuál es el orden de cada caracter
#de acuerdo a como lo reconoce Python
nombre = "alejandro"
index = 0
while index < len(nombre):
    x = nombre[index]
    print(index, x)
    index = index + 1

#Hace casi lo mismo de arriba, pero de una manera
#más elegante y fácil de corregir o entender
#por parte de otra persona.
nombre = "alejandro"
for letras in nombre:
    print (letras)

#Si quiero saber cuántas veces aparece determinado
#valor, puedo usar lo siguiente:
nombre = "alejandro"
cuenta = 0
for letras in nombre:
    if letras == "a":
        cuenta = cuenta + 1
print("la letra a aparece", cuenta, "veces")


#Puedo extraer partes de un texto con ":"

nombre = "Alejandro Antonio"
print(nombre[0:4])
#en el caso anterior, el caracter 4 no se
#incluye; Python lo interpreta como
#"hasta tal caracter pero sin inculuirlo"

#Si el segundo número es mayor a la cantidad
#de elementos q tengo, Pyhton simplemente para
#cuando se acaban los elementos
nombre = "Alejandro Antonio"
print(nombre[10:49])

#si no se indica alguno de los valores
#Python asume q es el primero o ultimo
nombre = "Alejandro Antonio"
print(nombre[3:])
print(nombre[:8])


#"in" puede usarse como operador lógico.
#Permite saber si un elemento hace parte
#de otro. También puede usarse dentro de
#un "if" statement
nombre = "Alejandro Antonio"
"a" in nombre
#la línea anterior no es necesaria... simple/
#arroja un valor de T or F q no se ve
if "a" in nombre:
    print("a se encuentra dentro del nombre")


nombre = "Alejandro Antonio"
"k" in nombre
if "k" in nombre:
    print("k se encuentra en nombre")
else:
    print("k no se encuentra dentro del nombre")

#Tambien funciona con varios caracteres
nombre = "Alejandro Antonio"
if "ndr" in nombre:
    print("ndr se encuentra en nombre")

#Se pueden convertir mayúsculas en minúsculas
nombre = "Alejandro Antonio"
nombre_minuscula = nombre.lower()
#en la anterior línea le estoy pidiendo a Python
#que copie un string y lo devuelva en minúsculas
print (nombre_minuscula)

#O se pueden convertir minúsculas en mayúsculas
nombre = "Alejandro Antonio"
nombre_mayuscula = nombre.upper()
#en la anterior línea le estoy pidiendo a Python
#que copie un string y lo devuelva en minúsculas
print (nombre_mayuscula)

#Se pueden hacer muchas cosas más, una de ellas
#es reemplazar
nombre = "Alejandro"
nombrecompleto = nombre.replace("Alejandro","Alejandro Antonio")
print (nombrecompleto)

#Buscar en qué posición están determinado elemento
nombre = "Alejandro"
posicion = nombre.find("ndr")
print(posicion)

#Eliminar espacios en blanco de un str
nombre="   Alejandro   "
print(nombre)
nombresinespacio = nombre.strip()
print(nombresinespacio)

#Concatenar str´s:
nombre1 = "Alejandro"
nombre2 = "Antonio"
apellidos = "Naranjo Gaviria"

nombrecompleto = nombre1 + " " + nombre2 + " " + apellidos
#Debo generar espacios " " entre str si los requiero
print(nombrecompleto)
