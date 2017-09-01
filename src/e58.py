


def e58(length):
    max_primes = length ** 2 + 1
    
    
    is_prime = [False, False]
    for i in range(2, max_primes+1):
        is_prime.append(True)
        
        
    n = 2
    while n <= max_primes:
        if is_prime[n]:
            for i in range(n+n, max_primes+1, n):
                is_prime[i] = False
        n += 1
    
    
    grid = []
    
    for i in range(length):
        row = []
        for j in range(length):
            row.append(None)
        grid.append(row)
        
    
    
    
    
    
    trans = [[-1,0],[0,-1],[1,0],[0,1]]
    trans_index = 0
    
    x = length-1
    y = length-1
    n = length ** 2
    
    
    def next_coords_valid(x, y):
        x += trans[trans_index][0]
        y += trans[trans_index][1]
        if x >= length or y >= length:
            return False
        if x < 0 or y < 0:
            return False
        if not grid[x][y] == None:
            return False
        
        return True
    
    while n > 0:
        if not next_coords_valid(x, y):
            trans_index += 1
            if trans_index == 4:
                trans_index = 0
                
        grid[x][y] = n
        x += trans[trans_index][0]
        y += trans[trans_index][1]
    
        n -= 1
    
                
    d = length*2-1
    n = 0
    for i in range(length):
        if is_prime[grid[i][i]]:
            n += 1
        if is_prime[grid[length-1-i][i]]:
            n += 1
            
    return n/d
          
          
          
import time
start = time.time()  
            
            
max_primes = 10000000
     
is_prime_sieve = [False, False]
for i in range(2, max_primes+1):
    is_prime_sieve.append(True)
 
n = 2
while n <= max_primes:
    if is_prime_sieve[n]:
        for i in range(n+n, max_primes+1, n):
            is_prime_sieve[i] = False
    n += 1
    
prime_list = []
for i in range(2, max_primes):
    if is_prime_sieve[i]:
        prime_list.append(i)
                                  
import math

def is_prime(n):
    for i in prime_list:
        if n == i: 
            return True
        if n % i == 0:
            return False
        if n < i:
            break
    for j in range(i, int(math.sqrt(n))):
        if n % j == 0:
            return False
    return True
 
end = time.time()
diff = end-start
print("done sieve: time sec = %f" % diff)

             
x = 9
total_primes = 3
diff = 2
length = 3


stats = [1,1,1,0]
 
 
# while x < 1000000:
while total_primes / (2*length-1) > 0.1:
    length += 2
    diff += 2
 
    for i in range(4):
        x += diff 
        if is_prime_sieve[x]:
            total_primes += 1
            stats[i] += 1
     
#     print("ratio for length %d: %f" % (length, (total_primes / (2*length-1))))
     
     
print("ratio: %s length: %s" % ((total_primes / (2*length-1)), length))
print("stats: %s" % stats)
             
             
end = time.time()
diff = end-start
print("time sec: %f" % diff)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            