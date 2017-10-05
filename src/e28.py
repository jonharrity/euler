

def all(x):
    return 16*x*x + 4*x + 4

def total_sum(x):
    if x == 0:
        return 1
    else:
        return all(x) + total_sum(x-1)
    
def alg():
    print(total_sum(1))
    print(total_sum(2))
    print(total_sum(3))
    print(total_sum(4))
    


def f(n):
    print(1 + n**3*16/3 + 4*n*n + 4*n - 10.333)
def alg2():
    f(3)
    
def alg3():
    print(f3(1))
    print(f3(2))
    print(f3(3))
    print(f3(4))

def f3(n):
    return 1 + 24*n + 20*tri(n-1) + 32*tri(tri(n-1))

def tri(n):
    return int(n*(n+1)/2)

    
#669171001
if __name__ == '__main__':
    import metric
    metric.Metric([alg,alg3])
    
    
    
