'''
1)	Faça um programa para ler e imprimir 
uma matriz 2 × 4 de números inteiros.
'''
#int matriz[][] = new int[2][4]; JAVA
#               COL              LIN
import random
matriz = [[0] * 4 for i in range(2)]

for lin in range(2):
    for col in range(4):
        matriz[lin][col] = random.randint(0,100)
#print(matriz)

for lin in range(2):
    for col in range(4):
        print(matriz[lin][col], end=" ")
    print()