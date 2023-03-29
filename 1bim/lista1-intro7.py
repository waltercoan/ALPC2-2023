'''
7)	Faça um programa que receba dez 
números e armazene em uma lista. 
Em seguida copie todos os números 
da primeira lista para uma segunda 
lista, mas na ordem invertida da 
primeira lista.
'''
lista = [0] * 10
inv = [0] * 10
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())
#for i in range(9,-1,-1):
#    print(lista[i])
for i in range(0,10):
    inv[i] = lista[9-i]
print(inv)

#inv[0] = lista[9]
#inv[1] = lista[8]
#inv[2] = lista[7]
#inv[3] = lista[6]

'''
contador2 = 9
for i in range(0,10):
    inv[i] = lista[contador2]
    contador2 = contador2 - 1
print(inv)

'''
