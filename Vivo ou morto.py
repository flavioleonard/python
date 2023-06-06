P, R = map(int, input().split())
fila = map(int, input().split())
lista = []

for i in range(R):
    comando = list(map(int, input().split()))
    lista.append(comando[2:])
    print(lista)
    
    
