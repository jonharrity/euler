N = 100


def main():
	a = sum([x*x for x in range(1, N+1)])
	b = sum([x for x in range(1, N+1)]) ** 2

	print(b - a)

if __name__ == '__main__':
	main()

