#escopo global
numero = 1
#import os
#print(os.environ['senha'])

def alteraNumeroOriginal():
    #escopo LOCAL
    numero = 3

def alteraNumero():
    #transforma a variavel em global
    global numero
    numero = 3

numero = 2
alteraNumero()
alteraNumeroOriginal()
print("O valor e", numero)
