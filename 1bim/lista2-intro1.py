'''
Faça um programa que carregue dois vetores 
de dez elementos numéricos cada um e 
mostre um vetor resultante da intercalação 
desses dois vetores.
'''
listaA = [0] * 10
listaB = [0] * 10
result = [0] * 20
for i in range(10):
    print("Digite um numero")
    listaA[i] = int(input())
for i in range(10):
    print("Digite um numero")
    listaB[i] = int(input())

proxlivre = 0
for i in range(10):
    result[proxlivre] = listaA[i]
    proxlivre = proxlivre + 1
    result[proxlivre] = listaB[i]
    proxlivre = proxlivre + 1

print(result)

