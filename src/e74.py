
fac_map = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
# loops = [145, 169, 363601, 1454, 871, 45361, 872, 45362]
loops = [145, 169, 871, 872]

def get_next(n):
    return sum(fac_map[int(s)] for s in str(n))

def get_chain(start):
    chain = [start]
    n = get_next(start)
    while not n in chain:
        chain.append(n)
        n = get_next(n)
    return chain


if __name__ == '__main__':
    count = 0
    for i in range(10**6):
        if len(get_chain(i)) == 60:
            count += 1
    print(count)