"""
note:
n/phi(n) increases with the amount of unique primes, and decreases with each 
degree those primes are subject to
f(n) = n/phi(n)

f(2) < f(6) < f(30) < f(210) . . .
-> 510510


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


def main():
    max = 3
    max_i = 6
    
    for i in range(6, 1000, 1):
        n = i / phi(i)
        if n > max:
            max = n
            max_i = i
            
    print("max: %s   n=%s" % (max, max_i))
    
    
if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print("\ntotal time sec: %s" % (end-start))