import math



def primes_under(cap):
	is_prime = [False, False] + [True]*(cap-1)
	i = 2
	while i < math.sqrt(cap):
		for j in range(i+i, cap+1, i):
			is_prime[j] = False
		i += 1
		while not is_prime[i]:
			i += 1

	primes = []
	for i in range(2, cap+1):
		if is_prime[i]:
			primes.append(i)
	return primes

def main():
	N = 600851475143
	small_primes = primes_under(100000)
	
	largest = 2
	for p in small_primes:
		if N % p == 0:
			largest = p
			N = N // p
	print(largest)

if __name__ == '__main__':
	main()

