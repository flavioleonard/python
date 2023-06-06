num = int(input())
t = 1
if 1 <= num <= 1000:
    while num != 0 and 1 <= num <= 1000:
        print(f'Teste {t}')
        n1 = str(input())
        n2 = str(input())
        if 1 <= len(n1) <= 10 and 1 <= len(n2) <= 10:
            for c in range(1, num+1):
                a, b = map(int, input().split())
                if 0 <= a <= 5 and 0 <= b <= 5:
                    soma = a + b
                    if soma % 2 == 0:
                        print(n1)
        
                    else: 
                        print(n2)
                else:
                    print('')
        print('')
        num = int(input())
        t += 1
else:
    print('')
        
