#La función "def" permite crear funciones
#Precaución con "reserved words" de Python
def alejo():
    print("Alejandro Antonio")
    print("Naranjo Gaviria")
    print("1983 - 07 - 11")

alejo()

print("otra cosa")

alejo()


#la función "max" y "min" devuelven el elemento
#que sea más grande y el menor del argumento que se introduzca

LetraMayor = max("Alejandro Antonio Naranjo Gaviria")
#El caracter menor es un espacio... no la A
LetraMenor = min("Alejandro Antonio Naranjo Gaviria")
#A continuación no va a leer números sino un texto
#el mayor no es 1983 sino 9
NumeroMayor = max("1983 - 07 - 11")
NumeroMenor = min("1983 - 07 - 11")

#def permite definir la función pero no la ejecuta.
#es necesario invocarla para verla trabajando.
#print() por ejemplo, es una manera de invocar funciones creadas
print(LetraMayor)
print(LetraMenor)
print(NumeroMayor)
print(NumeroMenor)



#Es posible definir funciones que se ejecuten
#de manera condicional, dependiendo del parámetro
#que introduzca usuario
def saludar(lenguaje):
    if lenguaje == "es":
        print("Hola")
    elif lenguaje == "pt":
        print("Oi")
    else:
        print("Hello")

saludar("es")
saludar("pt")
saludar("wl")



#Función "return" devuelve un determinado valor...
#como lo entiendo, se parece a crear una variable,
#solo q es más compleja, porque es lo que le pido al programa
#que haga dependiendo de los procesos que se llevan a cabo
#al interior de la función (como analizar un texto y pedirle
#que me diga cuál es el caracter mayor... función "max()")
#los ejemplos a continuación son muy básicos y hacen ver como
#excesiva esta función, pero en otras cosas más complejas
#empieza a ser útil
def saludar():
    return "Buenos dias como estas?"

print(saludar(), "Alejo")
print("Alejo", saludar())


#aquí va una un poco más compleja:
def saludar(lenguaje):
    if lenguaje == "es":
        return "Hola"
    elif lenguaje == "pt":
        return "Oi"
    else:
        return "Hello"

print(saludar("en"), "Bob")
print(saludar("es"), "Antonio")
print(saludar("pt"), "Bruno")



#Esta por ejemplo es una fxn para sumar parámetros:
def sumardos(a, b):
    suma = a + b
    return suma

x = sumardos(4, 6)
print(x)

x = sumardos(5, 9)
print(x)
