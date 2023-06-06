N = int(input())
lista = []
n = 0
soma = 0
for i in range(N):
    L, C = map(int, input().split())
    if L > C:
        lista.append(C)
        
for j in lista:
    soma += j
print(soma)
    
