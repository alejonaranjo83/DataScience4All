cantidad = 0
sumatoria = 0.0

while True:
    textoEntrada = input("Ingrese un numero: ")
    if textoEntrada == "listo":
        break
    try:
        NumeroEntrada = float(textoEntrada)
    except:
        print("Entrada no permitida")
        continue
    cantidad = cantidad + 1
    sumatoria = sumatoria + NumeroEntrada

print(sumatoria,cantidad,sumatoria/cantidad)
