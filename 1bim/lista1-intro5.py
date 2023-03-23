'''
5)	Faça um programa que receba dez 
números e armazene em uma lista. 
Em seguida percorra toda a lista 
e procure qual o MAIOR valor 
dentro da lista e qual o MENOR 
valor dentro da lista. No final
 apresente o MAIOR e o MENOR valor.
'''
lista = [0] * 10
omaior = 0
omenor = 0

for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())

#omaior = lista[0]
#omenor = lista[0]

for i in range(10):
    if i == 0: #estou na primeira volta
        omaior = lista[i]
        omenor = lista[i]
    if lista[i] > omaior:
        omaior = lista[i]
    #NUNCA MISTURAR O MAIOR COM O MENOR
    if lista[i] < omenor:
        omenor = lista[i]

print("O maior numero e ", omaior)
print("O menor numero e ", omenor)