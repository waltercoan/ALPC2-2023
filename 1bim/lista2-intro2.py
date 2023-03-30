conjx = [0] * 10
conjy = [0] * 10
for i in range(10):
    print("Posicao: ",i)
    repete = True
    while repete:
        print("Digite um numero")
        novonumero = int(input())
        for j in range(10):
            if novonumero == conjx[j]:
                print("Numero duplicado")
                repete = True
                break
        if j == 9:    
            repete = False
            print("Numero inserido")
            conjx[i] = novonumero
#AQUI OHHH




