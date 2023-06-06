m = int(input())
lista = []
lista1 = []
n = 0
for i in range (m):
    pg = list(map(float, input().split()))
    lista.append(pg)
    x = (lista[i][0]*1000)/lista[i][1]
    
for j in range(m):
    y = lista[j][0]*1000/lista[j][1]
    lista1.append(y)
    
lista1.sort()
print(f'{lista1[0]:.2f}')
        


    
    
