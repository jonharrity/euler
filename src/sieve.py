

import math


#defaults to using sievee of atkin
def get_primes(is_prime=None,max_prime=None):
    if not is_prime:
        if not max_prime:
            return None
        else:
            is_prime = sieve_atkin(max_prime)
    primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)
    return primes

def sieve_atkin(max_prime):
    is_prime = [False] * (max_prime+1)
    is_prime[2:4] = [True,True]
    sqrt_max = math.ceil(math.sqrt(max_prime))
        
    for x in range(1, sqrt_max+1):
        for y in range(1, sqrt_max+1):
            n = 4*x*x + y*y
            if n <= max_prime and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            
            n = 3*x*x + y*y
            if n <= max_prime and n % 12 == 7:
                is_prime[n] = not is_prime[n]
                
            n = 3*x*x - y*y
            if x > y and n <= max_prime and n % 12 == 11:
                is_prime[n] = not is_prime[n]
                
    for n in range(5, sqrt_max):
        if is_prime[n]:
            step = n*n
            for i in range(step, max_prime, step):
                is_prime[i] = False
                
    return is_prime



def sieve_eratosthenes(max_prime):
    is_prime = [True] * (max_prime+1)
    is_prime[:2] = [False]
        
    n = 2
    while n <= max_prime/2:
        for i in range(n+n, max_prime, n):
            is_prime[i] = False
        n += 1
        while not is_prime[n]:
            n += 1
            
    return is_prime


def sieve_eratosthenes2(max_prime):
    is_prime = [True] * (max_prime+1)
    is_prime[:2] = [False]
        
    n = 2
    while n <= max_prime/2:
        for i in range(n+n, max_prime, n):
            is_prime[i] = False
        n += 1
        while not is_prime[n]:
            n += 1
            
    return is_prime


def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def sundaram3(max_n):
    numbers = [i for i in range(3, max_n+1, 2)]
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + [i for i in filter(None, numbers)]



if __name__ == '__main__':
    
    limit = 10**8
    def f():
        l = sieve_for_primes_to(limit)
    def g():
        l = sundaram3(limit)
    import metric
    metric.Metric([f,g])






















