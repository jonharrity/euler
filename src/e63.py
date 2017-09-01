

def get_digit_count(n):
    return len(str(n))

count = 0

for n in range(1,10000):
    i=1
    while get_digit_count(i**n) <= n:
        if get_digit_count(i**n) == n:
            count += 1
        i += 1
        print(count)