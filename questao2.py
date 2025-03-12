def vef_fibb(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b #calcula o novo valor de fibbonaci
    return False

numero = int(input("Digite o número que deseja avaliar: "))

if(vef_fibb(numero)):
    print(f"O número {numero} pertence a sequencia de Fibonacci.")
else:
    print(f"O número {numero} não pertence a sequencia de Fibonacci")


