#7.1 Write a program that prompts for a file name,
#then opens that file and reads through the file,
#and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
#You can download the sample data at
#http://www.py4e.com/code3/words.txt

filename = input("Introduzca nombre archivo: ")
#se usa try/except en caso que usuario se equivoque
#al introducir nombre de archivo
try:
    filehandle = open(filename)
except:
    print ("File", filename, "cannot be opened")
    quit()

#for/in se usa para que líneas aparezcan
#en renglones diferentes
for textolineas in filehandle:
    #rstip elimina lo q está a la derecha, en este caso
    #newline characters \n
    textolineas = textolineas.rstrip()
    #upper pone todo el texto en mayúscula
    textolineas = textolineas.upper()
    print(textolineas)
