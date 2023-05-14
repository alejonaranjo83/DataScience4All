# 10.2 Write a program to read through the
# mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line
# by finding the time and then splitting the
# string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5
# 09:14:16 2008

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.


# Desired Output:
# 04 3
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# Como lo entiendo/traduzco:
# Busque dentro del archivo X la hora en que se enviaron
# los mensajes. 1). Ese valor está en las líneas que empiezan
# con "From ", para lo cual 2) hay que dividirla en palabras
# y extraer el 5to elemento. 3) Ese elemento lo debo volver
# a dividir pues solo interesan los dígitos de la hora.
# 4) Contar la cantidad de veces en que se mandan mail´s en c/hora
# e 5) imprimirlo en orden de horas


nombre = input("Introduzca nombre archivo: ")
portal = open(nombre)
dic = dict()

for lineasFrom in portal:
    if not lineasFrom.startswith("From "):
        continue
    From = lineasFrom.split()
    HoraFull = From[5]
    #Hasta aquí salen filas con hora/minuto/seg completa
    DivHora = HoraFull.split(":")
    Hora = DivHora[0]
    if Hora not in dic:
        dic[Hora] = 1
    else:
        dic[Hora] = dic[Hora] + 1

for k,v in sorted(dic.items()):
    print (k,v)
