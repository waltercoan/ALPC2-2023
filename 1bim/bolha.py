lista = [9,8,7,5,3]

for i in range(0,4):
    print("i:",i)
    for j in range(i+1,5):
        print ("\t j:",j)
        if lista[i] > lista[j]:
            lista[i],lista[j] = lista[j],lista[i]
            #aux = lista[i]
            #lista[i] = lista[j]
            #lista[j] = aux
print(lista)

lista = [9,8,7,5,3]
lista.sort()
