# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes
# the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that
# maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

#name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)

#Desired Output
#cwen@iupui.edu 5

#Traducción de la manera como interpreto lo q se debe hacer:
#1. lea un archivo
#2. identifique las líneas "From "
#3. extraiga la segunda palabra
#4. genere un diccionario y cuente cuánta veces
# aparece cada una de ellas
#5. dígame cuál fue la palabra que más repitió
# junto con la cantidad de veces

nombre = input("Introduzca nombre archivo: ")
portal = open(nombre)
cuenta = dict()

for renglon in portal:
    if not renglon.startswith("From "):
        continue
    listarenglon = renglon.split()
    mail = listarenglon[1]

    if mail not in cuenta:
        cuenta[mail] = 1
    else:
        cuenta[mail] = cuenta[mail] + 1

CorreoMasRep = None
CantidadRepetCorreo = None
for key,value in cuenta.items():
    if CantidadRepetCorreo is None or value > CantidadRepetCorreo:
        CantidadRepetCorreo = value
        CorreoMasRep = key

print(CorreoMasRep, CantidadRepetCorreo)
