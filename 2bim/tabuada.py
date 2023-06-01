tabuada = lambda x,y: x * y

print(tabuada(2,7))
eusouumasimplesvariavel = tabuada
print(eusouumasimplesvariavel(7,9))


def geratabuada(tabuada, func):
    for i in range(10):
        print(func(tabuada,i))

geratabuada(7, tabuada)