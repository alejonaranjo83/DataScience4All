#RECORDANDO Y "DESMENUZANDO" PASOS EJERCICIO 07_02
#hay pasos q varío con relación a formulación original
#para jugar y entender qué pasa en ellos
#1. prompt con sus respectivos try/except
#2. generar variables sobre las cuales se calcula promedio (sumar valores y cantidad de líneas)
#3. generar loop finito (for/in)... crear variable sobre la q se itera dentro del archivo
#4. leer solamente los valores numéricos
#5. meter esos valores dentro de otra variable
#6. transformar esa variable en un float
#7. sumar esos floats la variable inicialmente creada para sumar valores
#8. print("Promedio de spam: ", suma/cantidad)


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

fname = input("Introduzca nombre archivo: " )
try:
    fhandle = open(fname)
except:
    print("Nombre de archivo errado")
    quit()

suma = 0
cantidadLineas = 0

print("Estos son los valores numericos en forma de STRINGs que tiene el archivo:")

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    NumerosStrings = line[18+2: ]
    NumerosStrings = NumerosStrings.rstrip()
    print(NumerosStrings)
    ValoresNumericos = float(NumerosStrings)
    suma = suma + ValoresNumericos
    cantidadLineas = cantidadLineas + 1

print("La cantidad de lineas con valores numericos es:",cantidadLineas)
print("Promedio de spam: ", suma/cantidadLineas)
