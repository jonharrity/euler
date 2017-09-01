n = 3
d = 7


a = (1000000 - 1000000%d) / d

n *= a
d *= a

#answer at this point is n-1 but we haven't proved that yet

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


for n1 in range(int(n), 1, -1):
    if gcd(n1, d) == 1:
        print(n1)
        break