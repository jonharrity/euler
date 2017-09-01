
def reverse(n):
    return int( str(n)[::-1])


def is_lychrel(n, iter_count):
    
    n += reverse(n)
    
    if n == reverse(n):
        return False
    
    if iter_count > 50: 
        return True
    else:
        return is_lychrel(n, iter_count+1)


print( sum( is_lychrel(n,0) for n in range(1, 10000) ) )
