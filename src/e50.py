

import math


    
def get_index_above(n, primes, start=None, pivot=None):
    if n <= 2:
        return 0
    if n <= 3:
        return 1
    if n <= 5:
        return 2
      
    if start == None:
        start = int(len(primes)/2)
        pivot = start
          
    if start < 0:
        start *= -1
        
    pivot = math.ceil(pivot/2)
    
    if primes[start] >= n:
        if primes[start] == n:
            return start
        elif primes[start-1] == n:
            return start-1
        elif primes[start-1] <= n:
            return start#ON POINT
        else:
            return get_index_above(n, primes, start-pivot, pivot)#OVERSHOT
    else:
        return get_index_above(n, primes, start+pivot, pivot)#UNDERSHOT

#INCLUSIVE
def get_prime_index_above(n, primes):
    return get_index_above(n, primes)


def is_prime(n, primes):
    index = get_prime_index_above(n, primes)
    return primes[index] == n



def get_primes_around(n, count, primes):
    above_count = int(count/2)
    below_count = int(count/2)
    if count % 2 == 1:
        below_count += 1
        
    above_start = get_prime_index_above(n, primes)
    below_start = above_start - below_count
        
    return primes[below_start:above_start] + primes[above_start:above_start+above_count]


def get_primes_from_count(count, primes):
    ans = []
    half = math.ceil(count/2)
    start = half
    val = sum(get_primes_around(primes[start], count, primes))
    while val <= primes[-1]:
        if is_prime(val, primes):
            ans.append(val)
        start += 1
        val = sum(get_primes_around(primes[start], count, primes))
            
    return ans


def alg():
    top = 10 ** 6
    is_prime = [False, False]
    for i in range(top-1):
        is_prime.append(True)
    
    n = 2
    count_max = 0
    current_sum = 0
    primes = []
    while n < top:
        primes.append(n)
        if current_sum <= top:
            current_sum += n
            count_max += 1
        for i in range(n+n, top, n):
            is_prime[i] = False
        n += 1
        while n < top and not is_prime[n]:
            n += 1

    
    for i in range(count_max, 420, -1):
        valid_primes = get_primes_from_count(i, primes)
        if valid_primes:
            print(valid_primes[-1])
            return
        

if __name__ == '__main__':
    import time
    start = time.time()
    alg()
    end = time.time()
    print('total time sec: %s' % (end-start))











