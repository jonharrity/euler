


def is_increasing(n):
    mod = n % 10
    n -= mod
    n /= 10
    while n > 0:
        if n % 10 > mod:
            return False
        mod = n % 10
        n -= mod
        n /= 10
    return True
         

def is_decreasing(n):
    mod = n % 10
    n -= mod
    n /= 10
    while n > 0:
        if n % 10 < mod:
            return False
        mod = n % 10
        n -= mod
        n /= 10
    return True

def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)


def main():
    bouncy = 0
    nonbouncy = 0
    n = 1
    while True:
        if is_bouncy(n):
            bouncy += 1
        else:
            nonbouncy += 1        
        if nonbouncy*99 == bouncy: break
        n += 1

    print(n)


if __name__ == '__main__':
    import time
    start = time.time()
    main()
    end = time.time()
    print('time %ss' % round(end-start,3))