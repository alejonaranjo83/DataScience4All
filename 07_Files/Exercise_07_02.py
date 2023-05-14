#7.2 Write a program that prompts for a file name,
#then opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values
#from each of the lines and compute the average of
#those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum
#in your solution.
#You can download the sample data at
#http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter
#mbox-short.txt as the file name.


filename = input("Introduzca nombre de archivo: ")
#protegiéndose ante errores de usuario al introducir nombre
try:
    filehandle = open(filename)
except:
    print("el archivo", filename, "no existe")

#creando variables sobre las que se hará la cuenta
promedio = 0
cuenta = 0

for line in filehandle:
    #trabajar solo con las líneas q interesan para el ejercicio
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #eliminar \n (new line character)
    line = line.rstrip()
    #extraer valores numéricos... q empiezan a partir
    #del caracter 20. Se almacenan en una nueva variable "NumLine"
    NumLine = line[18+2:]
    #convertir esos valores en "float" para poderlos sumar
    NumLine = float(NumLine)
    #dígame cuántas líneas cumplen con las condiciones
    cuenta = cuenta + 1
    #sume los valores de las líneas que cumplen con las condiciones
    promedio = promedio + NumLine


print("Average spam confidence:", promedio/cuenta)
