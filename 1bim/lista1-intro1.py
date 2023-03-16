'''
1)	Faça um programa que receba dez 
números e armazene em uma lista. 
Em seguida percorra toda a lista 
mostrando apenas os números que cujo 
valor seja superior a 10.
'''
#lista = [0,0,0,0,0,0,0,0,0,0]
lista = [0] * 10
for i in range(0,10):
    print("Digite um numero")
    lista[i] = int(input())
print(lista)

for i in range(0,10):
    if lista[i] > 10:
        print(lista[i])
