def quadrado(q):
    return q ** 2

def dobro(a):
    return a * 2

n = int(input('Digite um numero: '))
r = dobro(n)
r2 = quadrado(r)

print(f'Resultado: {r}')
print(f'O resultado ao quadrado é: {r2}')