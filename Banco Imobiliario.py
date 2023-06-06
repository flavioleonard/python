I, N = map(int, input().split())
iD = I
iF = I
iE = I
for i in range(N):
    x = list(map(str, input().split()))
    if len(x) == 3:
        if x[0] == 'C':
            if x[1] == 'D':
                iD -= int(x[2])
            elif x[1] == 'F':
                iF -= int(x[2])
            elif x[1] == 'E':
        
        if x[0] == 'V':
            if x[1] == 'D':
                iD += int(x[2])
            elif x[1] == 'F':
                iF += int(x[2])
            elif x[1] == 'E':
                iE += int(x[2])
       
    else:
        x[3] = int(x[3])
        if x[0] == 'A':
            if x[1] == 'F':
                if x[2] == 'E':
                    iF += x[3]
                    iE -= x[3]
                else:
                    iF += x[3]
                    iD -= x[3]
                    
            elif x[1] == 'D':
                if x[2] == 'E':
                    iD += x[3]
                    iE -= x[3]
                else:
                    iD += x[3]
                    iF -= x[3]
            elif x[1] == 'E':
                if x[2] == 'D':
                    iE += x[3]
                    iD -= x[3]
                else:
                    iE += x[3]
                    iF -= x[3]
    print(iD, iE, iF)
                
        
