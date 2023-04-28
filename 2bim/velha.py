matriz =[[' '] * 3 for i in range(3)]
jogador = "X"
while True:
    for lin in range(3):
        for col in range(3):
            print(matriz[lin][col], end="|")
        print("\n---------")
    print("Digite a linha")
    jogadalin = int(input())
    print("Digite a coluna")
    jogadacol = int(input())
    matriz[jogadalin-1][jogadacol-1] = jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
#arrumar e desenho do tabuleiro
#impedir jogada invalida
#impedir jogada repetida
#verificar quem ganhou
#verifica velha
#https://pt.wikipedia.org/wiki/Minimax