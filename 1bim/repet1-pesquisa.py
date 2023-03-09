'''
Faça um programa que receba a idade, a altura e o 
peso de 25 pessoas. Calcule e mostre:
- a quantidade de pessoas com idade superior a 50 anos
- a média das alturas das pessoas com idade entre 10 e 20 anos;
- a percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
'''
contapessoas = 0
conta2 = 0
somaalturas = 0
contamagrinhos = 0
for pessoa in range(0,25):
    print("Pessoa: ", pessoa+1)
    print("Digite a idade")
    idade = int(input())
    print("Digite a altura")
    altura = float(input())
    print("Digite o peso")
    peso = float(input())

    if peso < 40:
        contamagrinhos += 1

    if idade >= 10 and idade <= 20:
        #ACUMULADOR
        somaalturas = somaalturas + altura
        conta2 += 1 #conta2 = conta2 + 1

    if idade >= 50:
        #CONTADOR
        contapessoas = contapessoas + 1
print("A qtd total de pessoas com mais de 50 anos e ", contapessoas)
media = somaalturas / conta2
print("A media da altura das pessoa com 10 a 20 anos e ", media)

perc = (contamagrinhos * 100 ) / 25
print("O perc de pessoas com menos de 40kg e: ", perc)