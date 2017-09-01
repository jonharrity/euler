import time
start = time.time()


square_max = 12
squares = []
for i in range(square_max):
    squares.append(i*i)



max = 568

arrives_at_89 = []
for i in range(1, max+1):
    arrives_at_89.append(None)
 
 
known = [89, 145, 42, 20, 4, 16, 37, 58]
for i in known:
    arrives_at_89[i] = True
     

def square_sum(n):
    sum = 0
    for s in str(n):
        i = int(s)
        sum += squares[i]
        
    return sum
    

for i in range(2, max):
    circle = [i]
    n = square_sum(i)
    while not n in circle and arrives_at_89[n] == None:
        circle.append(n)
        n = square_sum(n)
  
          
          
    if arrives_at_89[n]:
        for i in circle:
            arrives_at_89[i] = True
    else:
        for i in circle:
            arrives_at_89[i] = False    
 
     

ans = 0

for i in range(2, 10000000):
     
    circle = [i]
    n = square_sum(i)
    while not n in circle and arrives_at_89[n] == None:
        circle.append(n)
        n = square_sum(n)
 
         
         
    if arrives_at_89[n]:
        ans += 1

 
 
print("total: %d" % ans)



end = time.time()
diff = end-start
print("time took sec: %f" % diff)







