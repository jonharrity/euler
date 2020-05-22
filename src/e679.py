
    

def S(n):
    if n <= 0:
        return
    elif n == 1:
        for c in 'aefr':
            yield c
    else:
        for s in S(n-1):
            for c in 'aefr':
                yield s + c

def f(n):

    perms = S(4)
    si = {}
    for s in perms:
        si[s] = 0

    for i in range(5, n+1):
        


    if n < 5:  
        return 0
    else:
        count = 0
        for word in ['free','fare','area','reef']:
            for 
        return f(n-1) + count


if __name__ == '__main__':
    print([s for s in S(4)])
