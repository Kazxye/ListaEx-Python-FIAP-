tabuada = int(input("Digite um número:"))
print(f"Tabuada do {tabuada}:")

for i in range(1, 11, 1):
    print(str(tabuada) + " x " + str(i) + " = " + str(tabuada * i))
    