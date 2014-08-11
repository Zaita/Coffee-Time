target= 1000000

for i in range(1,10000001):
    if '0' in str(i): continue        
    for j in range(1,10000001):
        if '0' in str(j): continue
        if (i * j) == target:
            print ('Factors: ' + str(i) + ' : ' + str(j))
            return
