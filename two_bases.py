
for i in range(100, 1000):
    base9 = ''
    base10 = i
    for j in range(0,3):
        r = base10 % 9        
        base10 = (base10 - r) / 9        
        base9 += str(int(r))

    if str(base9) == str(i):
        print('Found: ' + str(i) + '^10 == ' + str(base9)[::-1] + '^9')
        break


        
    
    
