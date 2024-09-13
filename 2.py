def numero_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    
    if b == n or n == 0:
        return (f"O numero {n} pertence a sequencia de fibonacci")
    else:
        return (f"O numero {n} não pertence a sequencia de fibonacci")

numero = int(input("Digite um numero: "))
print(numero_fibonacci(numero))
