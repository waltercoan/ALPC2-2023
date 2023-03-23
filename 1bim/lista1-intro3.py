'''
3)	Faça um programa que receba dez 
números e armazene em uma lista. 
Em seguida, substitua todos os 
números cujo valor seja menor que 
10 pelo valor ZERO. Imprima a lista em tela.
'''
lista = [0] * 10
#entrada
for i in range(0,10):
    print("Digite um numero")
    lista[i] = int(input())
#processamento (trocas)
for i in range(10):
    if lista[i] < 10:
        lista[i] = 0

#for count, item in enumerate(lista):
#    if item <10:
#        lista[count] = 0

#saida
print(lista)

## for(int i=0;i<10;i++){
# }
##for (var item : lista) {}