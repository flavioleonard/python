N, I, F = map(int, input().split())
lista = list(map(int, input().split()))
soma = 0
for i in range(N):
    for j in range(i+1, N):
        x = lista[i] + lista[j]
        if I <= x <= F:
            soma += 1
    
    
print(soma)
    



