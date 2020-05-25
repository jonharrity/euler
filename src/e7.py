import collections
import math

N = 10001

cache = collections.OrderedDict()
def is_prime(x):
	if type(x) != type(1):
		raise Exception(f'invalid type {type(x)}')
	if x < 2:
		return False

	global cache
	if x in cache:
		return True
	
	sqrt = math.sqrt(x)
	for prime in cache.keys():
		if x % prime == 0:
			return False
		if prime > sqrt:
			break
	
	# is prime
	cache[x] = None
	return True 
				
def main():
	count = 0
	i = 1
	while count < N:
		i += 1
		if is_prime(i):
			count += 1

	print(i)

if __name__ == '__main__':
	main()
