#print("texto")
#print(123)
#print(True)
#print(True,123,"texto")


def minhafuncao(*args):
    print(type(args))
    for item in args:
        print(item)
minhafuncao()
minhafuncao("texto")
minhafuncao(123)
#minhafuncao(True)
minhafuncao(True,123,"texto")
