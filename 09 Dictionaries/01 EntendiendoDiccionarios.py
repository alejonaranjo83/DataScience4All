#Diccionarios
#1:
Datos = dict()
Datos ["nombre"] = "Alejandro Naranjo"
Datos ["nacimiento"] = "1983-07-11"
Datos ["edad"] = 36
Datos ["mail"] = "alejonaranjo83@gmail.com"

print("Datos del diccionario:")
#Estos son los datos que hay dentro del diccionario con sus respectivos KEYS")
print(Datos)
print(" ")

print("Extracción de valores del diccionario:")
#Se pueden extraer valores específicos del diccionario, en este caso la edad"
print(Datos["edad"])
print(" ")

print("Añadir valor a la categoría edad:")
#También se puede reemplazar un valor dentro del diccionario,
#en este caso añadir 3 años a la edad")
Datos ["edad"] = Datos ["edad"] + 3
print(Datos)
print(" ")

print("Cuenta de la cantidad de repeticiones:")



#2. Diccionarios permiten contar la cantidad de veces que
#se repiten los valores al interior de los mismos

cuenta = dict()
nombres = ["alejo", "naranjo", "1983", "alejo", "1983", "1983"]
for nombre in nombres:
    #si el nombre no está en el diccionario, cuéntelo la 1ra vez
    if nombre not in cuenta:
        #aquí el nombre entra a formar parte del diccionario CUENTA
        cuenta[nombre] = 1
    #si ya está en diccionario, súmelo a la cantidad de veces q ya está
    else:
        #aquí el valor se ingresa nuevamente al diccionario
        #y aumenta la cantidad que hay del mismo
        cuenta[nombre] = cuenta[nombre] + 1
print(cuenta)
print(" ")




#3. Puesto que lo anterior se hace con mucha frecuencia,
#Python tiene la función GET q simplifica el proceso...
#evita tener que poner "IF/ELSE":

print("Cuenta con GET en vez de IF/ELSE")
cuenta = dict()
nombres = ["alejo", "naranjo", "1983", "alejo", "1983", "1983"]
for nombre in nombres:
    #Aquí el nombre se añade al diccionario "cuenta"
    cuenta [nombre] = cuenta.get(nombre, 0) + 1
    #vaya al diccionario "cuenta", use el "nombre" como KEY
    #el 0 aparece para los valores que no existan en el diccionario
    #... es un default para que no genere traceback.
    #Si el valor ya existe, se le añade 1; sino se cuenta la 1ra vez
print(cuenta)



#4. keys, values e items:
diccio = dict()
Palabras = ["el", "payaso", "corrió",  "después", "el", "carro", "y", "el", "carro", "corrió"]
for palabra in Palabras:
    diccio [palabra] = diccio.get(palabra, 0) + 1
print(diccio)
print(diccio.keys())
print(diccio.values())
print(diccio.items())

print("Python permite usar dos variables sobre las cuales iterar al mismo tiempo:")
cuenta = dict()
nombres = {'el': 3, 'payaso': 1, 'corrió': 2, 'después': 1, 'carro': 2, 'y': 1}
for aaa,bbb in nombres.items():
    #aaa puede nombrarse como K (de Key) y bbb como V (de Value)
    print(aaa, bbb)
