N = int(input())
entrada = []
resultado = []
soma = 0
for i in range (0, N):
        entrada.append(input().split())

for u in range(len(entrada)):
    somaN = 0
    somaR = 0
    for n in range(0, len(entrada[u])-2):
        sub = int(entrada[u][n+1]) - int(entrada[u][n+2])
        if sub < 0:
            somaN += sub
            
    for o in range(len(entrada[u])-1, 0, -1):
        sub = int(entrada[u][o]) - int(entrada[u][o-1])
        if sub < 0:
            somaR += sub
    if somaN >= somaR:
        resultado.append(somaN)    
    else:
        resultado.append(somaR)

lista = resultado[:]
lista.sort(reverse=True)

    
print(resultado.index(lista[0])+1)
