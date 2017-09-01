




def concatenated_product(n, length):
    s = str(n)
    for i in range(2, length+1):
        s += str(n*i)
    return s



def is_pandigital(n):
    return "".join(sorted(str(n))) == "123456789"



ans = 0

for a in range(1, 10):
    for i in range(1,9999):
        n = concatenated_product(i, a)
        if len(n) == 9 and is_pandigital(n):
            if int(n) > ans:
                ans = int(n)
                
print(ans)

