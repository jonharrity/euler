


import math
import eratosthenes


MAX = 1000000
MAX = 999999



def main():
    E = eratosthenes.Eratosthenes(MAX)
    
    count = 0
    prime_list = E.get_primes()
    for prime in prime_list:
        if is_circular(prime, E):
            count += 1

    print(str(count) + " circular primes")


def is_circular(n, E):
    length = len(str(n))
    for i in range(1, length):
        n = shift_right(n, length)
        if not E.isPrime[n]:
            return False
        
    return True
            
            
        
        
def shift_right(n, length):
    tail = n % 10
    n /= 10
    tail *= 10**(length-1)
    n += tail

    return math.floor(n)

#     7652 -> 
#         2
#         765.2   ->
#             2000
#             765
#                 ->
#                     2765






if __name__ == "__main__":
        main()




