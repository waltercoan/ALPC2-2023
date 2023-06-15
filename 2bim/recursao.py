
def conta(numero:int):
    print(numero)
    if numero < 100:
        conta(numero + 1)

conta(0)

