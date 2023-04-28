#JAVA
#int[][] matriz = new int[3][3];
#C#
#int[,] matriz = new int[3,3];

lista = [0] * 3
#matriz =[[0,0,0],[0,0,0],[0,0,0]]
matriz = [[0] * 3 for i in range(3)]
matriz[0][0] = 100
matriz[2][2] = 200
matriz[0][2] = 50
print(matriz)
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=" ")
    print()
for coluna in range(3):
    for linha in range(3):
        print(matriz[linha][coluna], end=" ")
    print()