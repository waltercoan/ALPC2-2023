'''
4)	Faça uma função que receba cinco valores
inteiros, e retorne o maior valor. Faça uma 
segunda função que receba também cinco 
valores e retorne o menor deles.
'''
def encontraMaior(*numeros):
    omaior = 0
    for i in numeros:
        if i > omaior :
            omaior = i
    return omaior
def encontraMenor(*numeros):
    omenor = numeros[0]
    for i in numeros:
        if i < omenor :
            omenor = i
    return omenor

encontraMenor = lambda *numeros : min(list(numeros))

#guardar_resultado = encontraMaior(1,2,3,4,5)
#print("O maior", guardar_resultado)
#print("O menor", encontraMenor(1,2,3,4,5))
lista = [0] * 5
for i in range(5):
    print("Digite um numero")
    lista[i] = int(input())
print("O maior", encontraMaior(*lista))
print("O menor", encontraMenor(*lista))

valor = True
#operador ternario
print("verdadeiro" if valor else "falso")