















def get_pentagonal_numbers():
    n = 0
    while True:
        n += 1
        yield int(n*(3*n-1)/2)
        
def get_hexagonal_numbers():
    n = 0
    while True:
        n += 1
        yield n*(2*n-1)





def alg1():
    get_pent = get_pentagonal_numbers()
    get_hex = get_hexagonal_numbers()
    
    pent_n = next(get_pent)
    hex_n = next(get_hex)
    
    for i in range(1, 4):
        while pent_n != hex_n:
            if pent_n > hex_n:
                hex_n = next(get_hex)
            else:
                pent_n = next(get_pent)
        pent_n = next(get_pent)
    
    print(pent_n)





if __name__ == '__main__':
    alg1()











