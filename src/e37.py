






import math
from eratosthenes import Eratosthenes

MAX = 1000000






E = Eratosthenes(MAX)




def is_truncatable(prime):
    length = len(str(prime))
    return _truncate_left(prime, length) and _truncate_right(prime, length)

def _truncate_left(prime, length):
    for i in range(1, length):
        s = str(prime)[1:]
        if len(s) == 0:
            return

        prime = int(s)
        if not E.isPrime[prime]:
            return False
        
    return True
    
def _truncate_right(prime, length):
    for i in range(1, length):
#         print("changing right from %s to %s" % (prime, math.floor(prime/10)))
        prime /= 10
        prime = math.floor(prime)
        if not E.isPrime[prime]:
            return False 
        
    return True
        
        
        
        
        
print("is truncatable 3797? %s ; it should be" % (is_truncatable(3797)))


10000
count = 1
sum = 0
for i in E.get_primes():
    if i < 10:
        None
    elif is_truncatable(i):
        sum += i
        print("found %s : %s ; sum = %s" % (count, i, sum))
        count += 1
        
        
        
        
        
        