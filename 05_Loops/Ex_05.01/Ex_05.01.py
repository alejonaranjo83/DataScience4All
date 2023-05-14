#5.2 Write a program that repeatedly prompts
#a user for integer numbers until the user
#enters 'done'. Once 'done' is entered, print out
#the largest and smallest of the numbers.
#If the user enters anything other than a valid
#number catch it with a try/except and put out an
#appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below


ElMayor = None
ElMenor = None

#loop infinito hasta q yo diga otra cosa
while True:
    #valor que pediré de manera iterativa
    NumeroStr = input("ingrese numero entero: ")
    #si se ingresa "done" se interrumpe iteración
    if NumeroStr == "done":
        break
    #si usuario ingresa valor permitido, transfórmelo en #entero
    try:
        Numero = int(NumeroStr)
    #en caso de q usuario ingrese valor no permitido
    except:
        print("Invalid input")
        #si ingreso valor malo, regrese a arriba
        continue

    #Hágame la cuenta de cuál fue el #mayor y menor
    if ElMayor is None:
        ElMayor = Numero
    elif Numero > ElMayor:
        ElMayor = Numero
    elif ElMenor is None:
        ElMenor = Numero
    elif Numero < ElMenor:
        ElMenor = Numero

#dígame cuáles fueron los #s mayores y menores
print("Maximum is", ElMayor)
print("Minimum is", ElMenor)
