flag = True
n = 0
while flag == True:
    N = int(input())
    n += 1
    print(f'Teste {n}')
    if 0 <= N <= 1000:
        try:
            n1 = str(input())
            n2 = str(input())
        except EOFError:
            pass    
        n = 1
        if 1 <= len(n1) <= 10 and 1 <= len(n2) <= 10:

            while N != 0:
                A, B = map(int, input().split())
                N -= 1
                if (A+B) % 2 == 0:
                    print(n1)
                else:
                    print(n2)

            print('')

        

    
         

