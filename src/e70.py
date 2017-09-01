"""
2 * phi(n) = phi(2n)

a * phi(n) = phi(a*n)
"""

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def phi(n):
    return sum(gcd(i, n) == 1 for i in range(1, n))


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))



def main():
    MAX = 10**7
    
    
    prime_max = 10 ** 4
    is_prime = []
    for i in range(prime_max+1):
        is_prime.append(True)
         
    primes = []
    n = 2
    while n < prime_max:
        primes.append(n)
        for i in range(n+n, prime_max, n):
            is_prime[i] = False
        n += 1
        while not is_prime[n]:
            n += 1
             
    print("%s primes found" % len(primes))
    
    

    n = 2
    phi_n = phi(n)
    
    for i in range(1, 1000):
        n = i
        phi_n = phi(n)
        for j in primes:
#         while n < MAX:
            if is_permutation(n, phi_n):
                print("n=%s, n and phi(n) are permutations" % n)
            n *= j
            phi_n *= j
        
            




if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print("total time sec: " + str(end-start))