

def is_palindrome(x):
	s = str(x)
	return s == s[::-1]

def main():
	largest = -1
	for i in range(100, 999):
		for j in range(100, 999):
			p = i*j
			if is_palindrome(p) and p > largest: 
				largest = p
	print(largest)	

if __name__ == '__main__':
	main()

