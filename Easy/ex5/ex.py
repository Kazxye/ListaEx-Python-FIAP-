def contagem_regressiva(n):
    if n >= 1:
        print(n)
        contagem_regressiva(n - 1)
    else:
        print("Final da contagem")

contagem_regressiva(10)