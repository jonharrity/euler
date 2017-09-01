
max = 10000




is_prime = []
for i in range(max+1):
    is_prime.append(True)
    
    
primes = []
n = 2
while n < max:
    if is_prime[n]:
        if n >= 1000 and n < max:
            primes.append(n)
            
        for i in range(n+n, max, n):
            is_prime[i] = False
    n += 1
    
    
    
def is_perm(a, b, c):
    a_set = set()
    for i in str(a):
        a_set.add(i)
        
    b_set = set()
    for i in str(b):
        b_set.add(i)
        
    c_set = set()
    for i in str(c):
        c_set.add(i)
        
    return a_set == b_set == c_set



for diff in range(int(max/3), 1, -1):
    for prime in primes:
        a = prime + diff
        b = a + diff
        if b > max:
            continue
        if is_prime[a] and is_prime[b] and is_perm(prime, a, b):
            print("difference %d, primes [%d, %d, %d]" % (diff, prime, a, b))