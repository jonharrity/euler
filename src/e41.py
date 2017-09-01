

def get_primes(lower, upper):
    is_prime = [False, False]
    for i in range(upper-1):
        is_prime.append(True)
    
    n = 2
    while n < upper:
        for i in range(n+n, upper, n):
            is_prime[i] = False
        n += 1
        while n < upper and not is_prime[n]:
            n += 1
    
    primes = []
    for i in range(lower, upper):
        if is_prime[i]:
            primes.append(i)
    return primes


def is_n_pandigital(n, num):
    global match
    return ''.join(sorted(str(num))) == match

def get_n_digit_pandigital_primes(n):
    lower = 10 ** (n-1)
    upper = lower * 10
    primes = get_primes(lower, upper)
    
    solutions = []
    for prime in primes:
        if is_n_pandigital(n, prime):
            solutions.append(prime)
    
    return solutions


def alg():
    global match
    match = '1234567'
    solutions = get_n_digit_pandigital_primes(7)
    print(solutions[-1])



if __name__ == '__main__':
    import time 
    start = time.time()
    alg()
    end = time.time()
    print('total time sec: %s' % (end-start))
    
    
    
    
    
    
    
    
    