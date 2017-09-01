






ans = 0
n, d = 3, 2
for i in range(0, 999):
    if len(str(n)) > len(str(d)):
        ans += 1
    n, d = n+2*d, n+d
print(ans)
