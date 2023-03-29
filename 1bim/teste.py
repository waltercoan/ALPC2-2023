def minhafuncao():
    print("coisa 1")
    print("coisa 2")
    raise Exception("Deu ruim")
    print("coisa 3")
    print("coisa 4")

try:
    minhafuncao()
except:
    print("Deu ruim")

