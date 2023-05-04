contas = [0] * 10
saldos = [0] * 10
contas = [1,2,3,4,5,6,7,8,9,10]
saldos = [10,20,30,40,50,60,70,80,90,100]

#cadastro das contas sem repetir codigos
#for C indica qual posicao da conta sera preenchida
for c in range(10):
    repete = True
    while repete:
        #solicito o novo numero da conta
        print("Digite o numero da conta")
        numero = int(input())
        #procurar se o numero ja foi cadastro
        i = 0
        #pasar por todas as posicoes
        while i < 10:
            #comparar o numero digitado com 
            #o numero da conta em cada casinha
            if numero == contas[i]:
                print("Conta duplicada")
                #paro de procurar
                break
            i = i + 1
        #se eu passar por todas as posicoes
        # e nao encontarar o i será igual a 10
        if i == 10:
            #o numero digitado nao e duplicado
            print("Conta cadastrada")
            #cadastra o novo numero de conta na lista
            contas[c] = numero
            repete = False
    #cadastra o saldo
    print("Digite o saldo")
    saldos[c] = int(input())

opcao = 0
while opcao != 4:
    print("Menu")
    print("1.	Efetuar depósito")
    print("2.	Efetuar saque")
    print("3.	Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)")
    print("4.	Finalizar o programa")
    print("Digite a opcao")
    opcao = int(input())
    if opcao == 1:
        #Deposito
        print("Digite o numero da conta")
        numero = int(input())
        print("Digite o valor do deposito")
        valdep = float(input())
        #procurar a conta pelo numero
        #passar por todas as contas
        i = 0
        while i < 10:
            #comparar cada numero de conta
            #com o numero da conta desejada para
            #deposito
            if numero == contas[i]:
                print("Conta encontrada")
                #aumento o saldo da conta
                saldos[i] = saldos[i] + valdep
                break
            i = i + 1
        #se i == 10 entao nao encontrei o
        #numero da conta
        if i == 10:
            print("Conta nao encontrada")
    if opcao == 2:
        print("Digite o numero da conta")
        numero = int(input())
        print("Digite o valor do saque")
        valsaq = float(input())
        #procurar pela conta
        i = 0
        while i < 10:
            #compara cada posicao
            if numero == contas[i]:
                print("Conta encontrada")
                #verificar o saldo
                if saldos[i] >= valsaq:
                    #se houver saldo faz saque
                    saldos[i] = saldos[i] - valsaq
                else:
                    print(f"saldo insuficiente - saldo {saldos[i]}")
                    print("saldo insuficiente - saldo ",saldos[i])
                break
            i = i + 1
        if i == 10:
            print("Conta nao encontrada")
    if opcao == 3:
        total = 0
        for i in range(10):
            print(f"Conta {contas[i]} saldo {saldos[i]}")
            total = total + saldos[i]
        print("O total e ", total)