contas = [0] * 10
saldos = [0] * 10
contas = [1,2,3,4,5,6,7,8,9,10]
saldos = [10,20,30,40,50,60,70,80,90,100]
'''
for c in range(10):
    repete = True
    while repete:
        print("Digite o numero da conta")
        numero = int(input())
        i = 0
        while i < 10:
            if numero == contas[i]:
                print("Conta duplicada")
                break
            i = i + 1
        if i == 10:
            print("Conta cadastrada")
            contas[c] = numero
            repete = False
    print("Digite o saldo")
    saldos[c] = int(input())
'''
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
        print("Digite o numero da conta")
        numero = int(input())
        print("Digite o valor do deposito")
        valdep = float(input())
        i = 0
        while i < 10:
            if numero == contas[i]:
                print("Conta encontrada")
                saldos[i] = saldos[i] + valdep
                break
            i = i + 1
        if i == 10:
            print("Conta nao encontrada")
    if opcao == 2:
        print("Digite o numero da conta")
        numero = int(input())
        print("Digite o valor do saque")
        valsaq = float(input())
        i = 0
        while i < 10:
            if numero == contas[i]:
                print("Conta encontrada")
                if saldos[i] >= valsaq:
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