puntaje = input("Ingrese valor entre 0.0 y 1.0:")
puntajeDecimal = float(puntaje)

if puntajeDecimal < 0.6:
    print("F")
elif puntajeDecimal < 0.7:
    print("D")
elif puntajeDecimal < 0.8:
    print("C")
elif puntajeDecimal < 0.9:
    print("B")
elif puntajeDecimal < 1:
    print("A")
else:
    print("Error: el puntaje introducido está fuera del rango")

quit()
