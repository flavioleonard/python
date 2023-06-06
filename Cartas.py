valores = list(map(int, input().split()))
lista = valores[:]
ic = 0
iD = 0 
n = 0 
lista.sort()
for i in range(len(valores)):
    valores[i] == lista[i]
    if valores[i] == lista[i]:
        ic += 1
if ic == len(valores):
    print('C')
lista.sort(reverse=True)
for j in range (len(valores)-1, -1, -1):
    if valores[j] == lista[n]:
        iD += 1
        n -= 1
        if iD == len(valores):
            print('D')

if iD != len(valores) and ic != len(valores):
    print('N')

    
