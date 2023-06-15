'''
2)	Faça uma função que transforme e 
mostre segundos em:
horas, minutos e segundos. 
Todas as variáveis devem ser passadas 
como parâmetro, não havendo variáveis 
globais.
a.	1h = 3600s
b.	1m = 60s
'''
def convsegundos(qtdseg:int):
    qtdhoras = int(qtdseg / 3600)
    sobraseg = qtdseg % 3600
    qtdmin = int(sobraseg / 60)
    segfinais = sobraseg % 60
    print(f"Horas: {qtdhoras} \
           Minutos: {qtdmin} \
           Segundos: {segfinais}")

print("Digite uma qtd de segundos")
segundos = int(input())
convsegundos(segundos)