x = int(input("Informe a cordenada x: "))
y = int(input("Informe a cordenada y: "))
if 0 < x < 10 and 0 < y < 10:
    print("Dentro do quadrado. ")
elif x == 0 or x == 10 or y == 0 or y == 10:
    print("Na fronteira. ")
else:
    print("Fora do quadrado. ")
