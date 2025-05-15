def fibonnaci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)
n = int(input("Digite um número: "))
print(f"A sequência de Fibonacci até {n} é:")
for i in range(n):
    print(fibonnaci(i), end=" ")