conjx = [0] * 10
conjy = [0] * 10
"""

for i in range(10): #i define a casa preenchida
    print("Posicao: ",i)
    repete = True
    while repete:
        print("Digite um numero")
        novonumero = int(input()) # solicita numero
        #procura
        for j in range(10): #j indica posicao procurada
            if novonumero == conjx[j]:
                print("Numero duplicado")
                repete = True
                break
        if j == 9:    
            repete = False
            print("Numero inserido")
            conjx[i] = novonumero
#AQUI OHHH
print("conjx: ", conjx)
for i in range(10):
    print("Posicao: ",i)
    repete = True
    while repete:
        print("Digite um numero")
        novonumero = int(input())
        for j in range(10):
            if novonumero == conjy[j]:
                print("Numero duplicado")
                repete = True
                break
        if j == 9:    
            repete = False
            print("Numero inserido")
            conjy[i] = novonumero
print("conjy: ", conjy)


''' opcao chatgpt
uniao = []
for i in conjx:
    if i not in uniao:
        uniao.append(i)

for i in conjy:
    if i not in uniao:
        uniao.append(i)
"""
#UNIÃO (todos os elementos de X e os elementos
#       de Y que nao estão em X)
conjx = [1,2,3,4,5,6,7,8,9,10]
conjy = [1,20,3,40,5,60,7,80,9,100]
uniao = [0] * 20
for i in range(10):
    uniao[i] = conjx[i]

proxlivre = 10
for i in range(10): #i indexador do conjY
    achei = False
    for j in range(10):
        if conjy[i] == conjx[j]:
            achei = True
            break
    #if achei == False:
    if not achei:
        uniao[proxlivre] = conjy[i]
        proxlivre += 1
print(uniao)

##b.	a diferença entre X e Y (todos os 
# elementos de X que não achei em Y)
diff = [0] * 10
proxlivre = 0
for i in range(10): #i - indexador do X
    achei = False
    for j in range(10): #j - indexador do Y
        if conjx[i] == conjy[j]:
            achei = True
            break
    #if achei == False:
    if not achei:
        diff[proxlivre] = conjx[i]
        proxlivre += 1
print("Diferenca: ", diff)

#c.	a soma entre X e Y (soma de cada 
# elemento de X com o elemento 
# de mesma posição em Y)

soma = [0] * 10
for i in range(10):
    soma[i] = conjx[i] + conjy[i]
print("Soma: ", soma)
