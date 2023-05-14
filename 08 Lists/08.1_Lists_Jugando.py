#1. Entendiendo LISTAS
#sacar promedio de número que se ingresan
#de manera aleatoria

#Se crea una lista en blanco
ListaNumeros = list()

#Loop que va a almacenar valores q introducirá usuario
#y se acaba cuando el usuario introduzca palabra "listo"
while True:
    inp = input("Introduzca valor: " )
    if inp == "listo" : break
    #debido a q valores inroducidos son "str" se
    #deben convertir en decimales
    Numeros = float(inp)
    #a la lista que se creó inicialmente, se le irán integrando
    #los numeros introducidos por el usuario con la fxn "append"
    ListaNumeros.append(Numeros)

#Puesto que los valores introducidos hacen parte de una lista,
#puedo usar fxn "sum" y "len" para que dichos valores se sumen
#entre sí (sum), se calcule la cantidad de elementos (len)
#y se calcule el promedio diviendo los 2 anteriores
promedio = sum(ListaNumeros) / len(ListaNumeros)
print("El promedio de los numeros introducidos es:",promedio)
print("La cantidad de elementos introducidos fue de:", len(ListaNumeros))
#Sobre las listas se pueden aplicar fxnes de max, min,
#extraer valores puntuales "slicing" y otras
print("El mayor valor introducido fue:", max(ListaNumeros))
print("El menor valor introducido fue:", min(ListaNumeros))
print("Los primeros 3 elementos son:", ListaNumeros[:3])
print("Los elementos que hay desde el 3ro hasta el final son:",ListaNumeros[2:])
print("Los elementos que hay desde el 3ro hasta el 5to:",ListaNumeros[2:5])
print(" ")




#2. Otro ejercicio: lista mezclada
print("Este es otro ensayo con listas:")

maleta = list()

while True:
    empacando = input("Introduzca el valor que desee en la maleta:", )
    if empacando == "listo" : break
    maleta.append(empacando)

print("Estos son los objetos que contiene la lista: ")
print(maleta)
print(" ")

print("También puedo reemplazar objetos dentro de la lista: ")
maleta [3] = "valor reemplazado"
print(maleta)
print(" ")

#3. O se pueden concatenar listas
lista1 = list()
lista2 = list()

while True:
    generando1 = input("Introduzca valores de la lista 1: ")
    if generando1 == "listo": break
    lista1.append(generando1)
print("estos son los elementos de la lista 1:",lista1)

while True:
    generando2 = input("Introduzca valores de la lista 2: ")
    if generando2 == "listo": break
    lista2.append(generando2)
print("estos son los elementos de la lista 2:",lista2)

print("cuando se concatenan ambas listas (lista1 + lista2) este es el resultado de la nueva lista:", lista1 + lista2)
print(" ")


#4. O averiguar si hay o no determinado elemento dentro de la lista
# 1 in lista1 o 1 not in lista1... devolverá un valor True or False

# o reorganizar elementos dentro de la lista con "sort"... nombrelista.sort
