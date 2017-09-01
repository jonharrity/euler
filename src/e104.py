from e32 import is_pandigital



import math

sqrt5 = math.sqrt(5)
phi = (1 + math.sqrt(5)) / 2


def is_pandigital(n):
    for i in range(1,10):
        if not str(i) in n:
            return False
    return True


def ends_are_pandigital(n):
    n = str(n)
    return is_pandigital(n[:9]) and is_pandigital(n[-9:])


#rightmost 9 digits of nth fibbonaci number 
def right9(n):
    return mod_exp(phi, n, 1000000000) / sqrt5

def mod_exp(b, e, m):
    c = 1
    while e > 0:
        if( e % 2 == 1 ):
            c = (c * b) % m
        e = e >> 1
        b = (b * b) % m
    return c



last_matrix = (1,1,1,0)
last_index = 1
def F(n):
#     return Fmatrix((1,1,1,0), n-1)[1]
    global last_matrix, last_index
    
    m = last_matrix
    for i in range(last_index, n):
        m = (m[0]+m[1], m[0], m[2]+m[3], m[2])
    
    last_matrix = m
    last_index = n
    
    return m[1]


def is_perfect_square(n):
    sqrt = math.sqrt(n)
    return sqrt == round(sqrt)


def is_fibbonaci(n):
    square5 = n**2 * 5
    return is_perfect_square(square5 + 4) or is_perfect_square(square5 - 4)



def main():
                
    b = 2
    Fa = 1
    Fb = 1
    
    Ftmp = 0
    found = 0
 
    while True:
        Ftmp = Fb
        Fb += Fa
        Fa = Ftmp
        b += 1

        Fa %= 1000000000
        Fb %= 1000000000

        s2 = str(Fb)
        if is_pandigital(s2):
            full_value = F(b)
            if is_pandigital(str(full_value)[:9]):
                print(b)
                found += 1
                if found == 2:
                    break
                
            
        

        


if __name__ == '__main__':
    import time
    start = time.time()
    main()
    end = time.time()
    print("time: %ss" % round(end-start, 3))
    
    
    
    
    