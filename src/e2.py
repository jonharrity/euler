

MAX = 4 * 10 ** 6


ans = 0

a = 1
b = 1

while b < MAX:
	if b % 2 == 0:
		ans += b
	c = a + b
	a = b
	b = c

print(ans)
