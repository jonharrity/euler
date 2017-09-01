
import math


max = 1000000

consecutive_count = 4#pivot point


is_prime = []
primes = []
for i in range(max+1):
    is_prime.append(True)

n = 2
while n < max/2:
    if is_prime[n]:
        primes.append(n)
        for i in range(n+n, max, n):
            is_prime[i] = False
            
    n += 1
        

dict = {}
for prime in primes:
    for power in range(1, int(math.log(max, prime))+1):
        for mult in range(1, int(max/prime**power)):
            n = (prime**power) * mult            
            try:
                if not prime in dict[n]:
                    dict[n].append(prime)
            except Exception:
                dict[n] = [prime]
                

previous = 0
count = 0
for i in dict:
        
    if len(dict[i]) < consecutive_count:
        continue
    
    if i - 1 == previous:
        count += 1
    else:
        count = 1
        
    previous = i
    
    if count == consecutive_count:
        print("first: %d" % (i-consecutive_count+1))
        quit()
        
print("nothing")







