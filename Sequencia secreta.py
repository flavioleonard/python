t = int(input())
lista = []
n = 1
for i in range (t):
    x = int(input())
    lista.append(x)

for j in range(t-1):
    if lista[j] != lista[j+1]:
        n += 1

print(n)
    
