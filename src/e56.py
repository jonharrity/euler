







def sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum


highest = 0


for i in range(99, 0, -1):
    for j in range(99, 0, -1):   
        n = i ** j
        if sum(i**j) > highest:
            highest = sum(i**j)
            index = i**j
            
        
print("highest: %d" % highest)