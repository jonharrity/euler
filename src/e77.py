

def ways(n, primes, ways_lookup):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    
    if ways_lookup[n] < 1:
        print('generating for %s'%n)
        ans = sum(ways(n-prime, primes, ways_lookup) for prime in get_primes_below(n, primes))
        if n in primes:
            ans += 1
        ways_lookup[n] = ans
        
    return ways_lookup[n]

def get_primes_below(n, primes):
    max_index = primes.index(get_max_prime_below(n, primes))
    return primes[:(max_index+1)]


def get_max_prime_below(n, primes, start=None):
    if n <= 2:
        return None
    
    if start == None:
        start = int(len(primes)/2)
    
    while start >= len(primes):
        start -= 1
    if len(primes) == 1:
        return primes[0]
    
    if primes[start] > n:
        return get_max_prime_below(n, primes[:start], start=int(start/2))
    elif primes[start] == n:
        return primes[start-1]
    elif primes[start] < n:
        return get_max_prime_below(n, primes[start:], start=int(start/2)+1)

def get_primes(max):
    is_prime = [False,False]
    for i in range(max-1):
        is_prime.append(True)
        
    n = 2
    while n < max/2+2:
        for i in range(n+n, max, n):
            is_prime[i] = False
        n += 1
        while not is_prime[n]:
            n += 1
    primes = []
    for i in range(max):
        if is_prime[i]:
            primes.append(i)
    return primes    




def alg2():
    MAX = 10
    primes = get_primes(MAX)
    
    ways_lookup = [0,0,1,1]
    for i in range(MAX-3):
        ways_lookup.append(0)
    
    ans = ways(MAX, primes, ways_lookup)
    print('ans: %s' % ans)
    
    
def alg1():
    MAX = 1000
    
    primes = get_primes(MAX)
        
    primes_max_coefficients = []
    for i in primes:
        primes_max_coefficients.append(int(MAX/i))
    primes_coefficients = [0 for i in range(len(primes))]
        
    highest_value = sum(primes[i]*primes_max_coefficients[i] for i in range(len(primes)))
    table = [0 for i in range(highest_value)]
    print('highest value: ' + str(highest_value))
    mult = 1
    for i in primes_max_coefficients:
        mult *= i
    print('mult:'+str(mult))

    coeffient_mod_index = 0
    
    val = 0
    count = 0
    while True:
        table[val] += 1
#         table[sum(primes[i]*primes_coefficients[i] for i in range(len(primes)))] += 1
        count += 1
        
        primes_coefficients[coeffient_mod_index] += 1
        
        if primes_coefficients[coeffient_mod_index] > primes_max_coefficients[coeffient_mod_index]:
            if coeffient_mod_index == 0:
                break
            else:
                primes_coefficients[coeffient_mod_index] = 0
        if coeffient_mod_index == len(primes)-1:
            coeffient_mod_index = 0
        else:
            coeffient_mod_index += 1
    print('done calc: %s modifications' % count)

    for i in range(len(table)):
        if table[i] > 3000:
            print("%s: %s" % (i, table[i]))
            
    
    
    
    
    

if __name__ == '__main__':
    alg2()    
    
    
    
    
    