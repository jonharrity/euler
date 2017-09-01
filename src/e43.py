
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def permute(s):    
    if len(s) == 1:
        yield s
    else:
        for i in range(len(s)):
            for y in permute(s[0:i] + s[i+1:]):
                yield s[i] + y
                
def does_match_property(pand):
    i = 1
    for divisor in [2,3,5,7,11,13,17]:
        n = int(pand[i:i+3])
        if not n % divisor == 0:
            return False
        i += 1
    return True

#16695334890
def alg1():
    import itertools
    total = 0
    for pand in itertools.permutations('0123456789'):
#     for n in permute('0123456789'):
        n = ''.join(pand)
        if does_match_property(n):
            total += int(n)
    print(total)






if __name__ == '__main__':
    import metric
    metric.Metric([alg1])



