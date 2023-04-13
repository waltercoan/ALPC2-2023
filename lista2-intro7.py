'''
Uma empresa possui ônibus com 48 lugares 
(24 nas janelas e 24 no corredor). Faça um programa
 que utilize dois vetores para controlar as poltronas
 ocupadas no corredor e na janela. Considere
 que zero representa poltrona desocupada e um 
 representa poltrona ocupada.

          +---+---+---+---+---+---+---+---+
JANELA    | 0 | 1 | 0 | 0 |   | 1 | 1 | 1 |
          +---+---+---+---+---+---+---+---+
Poltrona    1   2   3   4  ...  22  23  24
          +---+---+---+---+---+---+---+---+
CORREDOR  | 0 | 1 | 0 | 0 |   | 0 | 0 | 1 |
          +---+---+---+---+---+---+---+---+

Esse programa deve controlar a venda de passagens
da seguinte maneira:
O cliente informa se deseja poltrona no corredor 
ou na janela e, depois, o programa deve informar 
quais poltronas estão disponíveis para a venda;
	Quando não existirem poltronas livres 
    no corredor, nas janelas ou, ainda, 
    quando o ônibus estiver completamente 
    cheio, deve ser mostrada uma mensagem.

'''
janela = [0] * 24
corredor = [0] * 24

opcao = 0
while opcao != 4:
    print("Venda de passagens")
    print("1 - Vender passagem")
    print("4 - Sair")
    print("Digite a opcao desejada")
    opcao = int(input())

    if opcao == 1:
        print("Digite janela ou corredor")
        tipo = input()
        if tipo == "janela":
            for i in range(24):
                if janela[i] == 0:
                    print("Posicao livre: ", i+1)
            print("Qual posicao desejada")
            num = int(input())
            janela[num-1] = 1
        if tipo == "corredor":
            for i in range(24):
                if corredor[i] == 0:
                    print("Posicao livre: ", i+1)
            print("Qual posicao desejada")
            num = int(input())
            corredor[num-1] = 1
