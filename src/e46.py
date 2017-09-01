

# MAX = 10000000
MAX = 1000000

from eratosthenes import Eratosthenes


def main():
    
    E = Eratosthenes(MAX)
    prime_list = E.get_primes()
    
    sieve = E.isPrime
        
    sieve[1] = True        
        
    two_squares = []
    i = 1
    n = 1
    while n:
        n = 2*i*i
        if n > MAX:
            break
        two_squares.append(n)
        i += 1
        
        
        
    #takes little time
    for prime in prime_list:
        for square in two_squares:
            n = prime + square
                        
            if n >= MAX:
                break
            sieve[n] = True
            
            
    for i in range(1, MAX, 2):
        if sieve[i] == False:
            print("False at i=" + str(i))


if __name__ == "__main__":
    import time
    start = time.clock()
    
    main()
    
    end = time.clock()
    print("Time: " + str((end-start)))
    
    
    
    
    
    