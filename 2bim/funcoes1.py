def somanumeros(a:int, b:int, c:int):
    soma = 0
    for i in range(b,c+1):
        if i % a == 0:
            soma = soma + i
    return soma

guardar = somanumeros(2,10,100)
print(guardar)