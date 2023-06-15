'''
3)	Faça uma função que receba as três 
notas de um aluno como parâmetro e uma 
letra. Se a letra for A o procedimento 
calcula a média aritmética das notas do 
aluno, se for P o procedimento calcula a 
média ponderada com os pesos 5,3 e 2. A 
média calculada deve ser devolvida ao 
programa principal para, então, ser 
mostrada.
'''

def media(n1:float, n2:float, n3:float, tipo:str):
    resul_media = 0
    if tipo == 'a' or tipo == 'A':
        resul_media = (n1 + n2 + n3) / 3
    else:
        resul_media = ((n1*5) + (n2*3) + (n3*2)) / 10
    return resul_media

print("Digite a primeira nota")
nota1 = float(input())
print("Digite a segunda nota")
nota2 = float(input())
print("Digite a terceira nota")
nota3 = float(input())
print("Digite o tipo da media (A ou P)")
tipo = input()
guardar_resultado = media(nota1, nota2, nota3, tipo)
print("Media ", guardar_resultado)