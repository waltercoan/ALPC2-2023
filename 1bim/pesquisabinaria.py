lista = [10,20,30,40,50]

for i in range(0,len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            #lista[i],lista[j] = lista[j], lista[i]

#LISTA DEVE ESTAR ORDENADA
print("Digite o numero procurado")
procurado = int(input())
ini = 0
#fim = 4 #ultima casa da lista
fim = len(lista) - 1
while ini <= fim:
    meio = int((ini + fim) / 2)
    if procurado == lista[meio]:
        print("Achei")
        break
    if procurado > lista[meio]:
        ini = meio + 1
    if procurado < lista[meio]:
        fim = meio - 1
if not ini <= fim:
    print("Não encontrado...")