#Tuples se pueden asignar valores entre expresiones:

(x,y) = (4,"alejo")
print(y)

#permiten hacer comparaciones (mayor, menor):
(0,3,5)>(2,3,5)
#Dará FALSE

#Evaluación la empieza a hacer según la posición
#de cada elemento del tuple, vs la misma posición
#en el otro tuple:
("Alejo", "Naranjo") > ("Alejo", "Gaviria")
#Devolverá valor TRUE
#El pcso anterior es así: Alejo = Alejo,
# N > G ... True
#Independiente de que los otros valores no cumplan
#con esta condición, ya se había comprobado N > G


#Esto es útil para por ejemplo organizar diccionarios
#según determinados criterios:

dic = {"a":3, "b":4, "c":13}
print("Al imprimir diccionario, sus tuples aparecen en desorden")
print(dic.items())
print("Si se quiere organizarlos, se puede usar SORTED")
print(sorted(dic.items()))
print("esto permitirá imprimir elementos en orden, de acuerdo a KEYS")

print("Si los quisiera en líneas separadas, lo que hago es generar un loop finito:")

for k,v in sorted(dic.items()):
    print (k,v)

print(" ")

#Si quisiera ordenarlo pero en fxn de sus valores
#debo generar un nuevo TUPLE construido al revés
#Value-Key que entra a formar parte de una lista
dic = {"a":3, "b":4, "c":13}
listaVK = list()
for k,v in dic.items():
    listaVK.append((v,k))

print(listaVK)

print("Impresión de lista Value-Key en orden ascendente:")
listaVK = sorted(listaVK)
print(listaVK)
print("Impresión de lista en orden descendente:")
listaVK = sorted(listaVK, reverse=True)
print(listaVK)
