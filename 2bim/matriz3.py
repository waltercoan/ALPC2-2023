'''
3)	Dada a seguinte matriz, calcule:
- A soma dos elementos de primeira coluna;
- O produto dos elementos da primeira linha;
- A soma de todos os elementos;
- O produto da diagonal principal.
'''
matriz = [[0] * 4 for i in range(4)]
cont = 1
for lin in range(4):
    for col in range(4):
        matriz[lin][col] = cont
        cont += 1
for i in range(4):
    print(matriz[i])

#A soma dos elementos de primeira coluna;
soma = 0
for lin in range(4):
    soma += matriz[lin][0]
    #soma = soma + matriz[lin][0]
print("A soma da primeira coluna e", soma)

#O produto dos elementos da primeira linha;
prod = 1 
for col in range(4):
    prod *= matriz[0][col]
print("O produto da primeira linha e", prod)

#A soma de todos os elementos;
soma = 0
for lin in range(4):
    for col in range(4):
        soma += matriz[lin][col]
print("Soma de todos os elementos", soma)

#- O produto da diagonal principal.
prod = 1
for i in range(4):
    prod *= matriz[i][i]
print("Produto da diagonal principal", prod)
prod = 1
for i in range(4):
    prod *= matriz[i][3-i]
print("Produto da diagonal secundaria", prod)
