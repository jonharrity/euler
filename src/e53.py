





def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
    
    
def nCr(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))



ans = 0

for n in range(1, 101):
    for r in range(1, n):
#         print("n: %d r:%d" % (n, r))
#         print(nCr(n, r))
        if nCr(n, r) > 1000000:
            ans += 1
print(ans)


