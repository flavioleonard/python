N = int(input())
P, C, Q = map(str, input().split())
if C == '*':
    x = int(P)*int(Q)
    
    if x >= N:
        print('OK')
    else:
        print('OVERFLOW')
else:
    x = int(P)+int(Q)
    if x >= N:
        print('OK')
    else:
        print('OVERFLOW')
    
