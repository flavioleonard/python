x = list(map(float, input().split()))
a = x[0]/x[2]
g = x[1]/x[3]

if a < g:
    print('A')
else:
    print('G')
