'''
2)	Faça um programa que receba dez números e 
armazene em uma lista. Em seguida conte quantos 
números são impar e quantos são par. Apresente 
os contadores na tela.
'''
contaimpar = 0
contapar = 0
lista = [0] * 10
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())
    
for i in range(10):
    if lista[i] % 2 == 1:
        contaimpar += 1
    else:
        contapar += 1

print("Numero de impares ", contaimpar)
print("Numero de pares ", contapar)