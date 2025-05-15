def verificar_numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return 'Numero não é primo'
    return 'Numero é primo'

print(verificar_numero_primo(7))
print(verificar_numero_primo(10))