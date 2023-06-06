N = int(input())
numeros = []
for i in range(N):
    n = input().split()
    numeros.append(n)
    senha = numeros[0][10:16]
print(senha)
