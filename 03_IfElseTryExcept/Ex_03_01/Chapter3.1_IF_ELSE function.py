#Entendiendo IF ELSE
x=1
if x>2:
    print("bigger")
else:
    print("smaller")
print "All done"



#ELIF (else if): sirve para analizar múltiples opciones
x=5
if x<3:
    print("chiquito")
elif x < 6:
    print("mediano")
elif x<12:
    print("grande")
elif x<24:
    print("muy grande")
else:
    print("gigante!")



x=6
if x == 6 :
    print("is 6")
    print("Is Still 6")
    print('Is Still 6')
    print("Third 6")



#Chapter 3 _ part 2
#Try and Except functions: cuando sé que hay
#una parte de un código que creo que puede fallar
Texto="Hola Alejo"
try:
    TextoNumero = int(Texto)
except:
    TextoNumero = -1

print("Primero que todo", TextoNumero)


Texto="1983"
try:
    TextoNumero = int(Texto)
except:
    TextoNumero = -1

print("Primero que todo", TextoNumero)


#Ejercicio más elaborado usando "Try/Except"
DatoSolicitado = input("digite numero:")
try:
    ValorInteger = int(DatoSolicitado)
except:
    ValorInteger = -1

if ValorInteger > 0:
    print("Bien hecho")
else:
    print("Error: escriba en número y no en letras")
