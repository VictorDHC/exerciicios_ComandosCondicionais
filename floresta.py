caminho = input("Você está perdido na floresta. Escolha seguir entre Direita ou Esquerda (dir/esq): ")
if caminho == "esq":
    rrio = input("Você encontrou um rio, atravessar ou voltar? (a/v) ")
    if rrio == "a":
        print("Parabéns, você encontrou uma vila segura! ")
    else:
        print("Você permanece perdido na floresta.. ")
if caminho == "dir": 
    bau = input("Você encontrou uma montanha. Subir ou voltar? (s/v): ")
    if bau == "s":
        print("Parabéns, você encontrou um tesouro! ")
    else:
        print("Você permanece perdido na floresta.. ")

