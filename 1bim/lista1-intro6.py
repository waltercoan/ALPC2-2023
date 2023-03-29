'''
6)	Faça um programa que receba dez números e
armazene em uma lista. Em seguida solicite um
outro número e armazene em uma variável chamada
multiplicador. Percorra todo a lista e multiplique
cada número pelo multiplicador e apresente em tela.
'''
lista = [0] * 10
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())
print("Digite o multiplicador")
multiplicador = int(input())
for i in range(10):
    result = lista[i] * multiplicador
    print(result)
