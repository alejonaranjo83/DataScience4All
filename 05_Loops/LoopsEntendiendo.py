#Precaución con "inifinite loops".
#Hay que aplicarles "break" xej
n = 5
while n > 0:
    print (n)
    n = n - 1
print("se acabó")
print(n)



#Finite loop. Con "for" Python toma el control
#de los loops (especifica cuándo debe hacer iteración)
#y facilita el proceso. En siguiente función,
#imprimira los diferente valores de "i"
#mientras existan elementos; una vez terminan,
#sigue con el resto del código

for i in [5,4,3,2,73]:
    print(i)
print("no hay más")


#También funciona con "strings". Ejecuta loop
#mientras hayan objetos dentro de la lista

amigos = ["Caliche", "Lili", "Jota", "Lalo"]
for amigo in amigos:
    print("Feliz navidad:", amigo)
print("no más de los verdaderos")



#Clave entender cómo piensan los computadores
#esto es, secuencial. A continuación va un ej

#

el_mas_grande = -1
print ("el mas grande antes", el_mas_grande)
for el_numero in [9, 41, 12, 3, 74, 15]:
    if el_numero > el_mas_grande:
        el_mas_grande = el_numero
    print(el_mas_grande, "es el mas grande hasta el momento", el_numero)
print("Finalmente este fue el mas grande", el_mas_grande)




#Encontrando el valor más pequeño... sin tener q ponerse
#a inventar números muy grandes para que funcione...
#se usa un tipo de variable conocido como "None" = ausencia de valor:

smallest = None
print("Before")
for value in[9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest, value)
print ("after", smallest)

#None solo aplica la primera vez... al inicio de la función
#luego el valor que me interesa se va transformando
#en función de lo que haya definido


#Encontrando el valor más grande... sin tener q ponerse
#a inventar números muy pequeños para que funcione (manera "elegante"):

masgrande = None
print("Before")
for value in[9, 41, 12, 3, 74, 15]:
    if masgrande is None:
        masgrande = value
    elif value > masgrande:
        masgrande = value
    print (masgrande, value)
print ("finalmente el mas grande fue", masgrande)
