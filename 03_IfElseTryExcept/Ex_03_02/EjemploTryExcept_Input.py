DatoSolicitado = input("digite numero:")
try:
    ValorInteger = int(DatoSolicitado)
except:
    ValorInteger = -1

if ValorInteger > 0:
    print("Bien hecho")
else:
    print("Error: escriba en número y no en letras")
