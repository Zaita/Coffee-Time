max_x = 0
max_y = 0
max_prod = 0

for i in range(1, 1024):
    x = ''
    y = ''

    binary = 1
    for j in range(0, 10):
        value = 9 - j
        
        if i & binary == binary:
            x = x + str(value)
        else:
            y = y + str(value)
        binary *= 2

    if x == '' or y == '':
        continue
    
    prod = int(x) * int(y)
    if (prod > max_prod):
        max_x = x
        max_y = y
        max_prod = prod

print (str(max_x) + ' * ' + str(max_y) + ' = ' + str(max_prod))

    
    
    
