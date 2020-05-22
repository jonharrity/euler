N = 20

def primes_under(x):
	is_prime = [False, False] + [True] * (x-1)
	i = 2
	while i <= x:
		for j in range(i+i, x+1, i):
			is_prime[j] = False
		i += 1
		while i <= x and (not is_prime[i]):
			i += 1

	primes = []
	for i in range(x+1):
		if is_prime[i]:
			primes.append(i)
	return primes


primes = primes_under(N)
def bag_add(bag, x):
	i = 0
	while x > 1:
		j = 0
		while x > 1 and x % primes[i] == 0:
			j += 1		
			x = x // primes[i]
		if j > bag[primes[i]]:
			bag[primes[i]] = j
		i += 1

def main():

	bag = [0] * (N+1)
	for i in range(1, N+1):
		bag_add(bag, i)
	
	ans = 1
	for i in range(1, N+1):
		if bag[i] > 0:
			ans *= i ** bag[i]

	print(ans)

if __name__ == '__main__':
	main()

