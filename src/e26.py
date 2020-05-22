import math

def decimals(number, precision):    
	dividend = 1
	count = -1
	s = ''
	while dividend and count < precision:      
		s += str(dividend // number)
		dividend = dividend % number * 10
		count += 1
	s = s[1:]
	return s
        


def get_cycle(x, l, cap):
	if len(l) < cap * 2:
		return 0
	
	reps_needed = math.ceil(math.log(x, 2)) + 2
	reps_needed = 4
	max_offset = math.ceil(math.log(x, 2)) 

	required_length = (x+1)*reps_needed + max_offset
	if len(l) < required_length:
		raise Exception('length %s < required length %s for int %s' % (len(l), required_length, x))

	for cycle_length in range(1,x+1):
		for a in range(max_offset):
			matches = 0
			for rep in range(reps_needed):
				s1 = l[a+rep*cycle_length:a+(rep+1)*cycle_length]
				s2 = l[a+(rep+1)*cycle_length:a+(rep+2)*cycle_length]
				if s1 == s2:
					matches += 1
				else:
					break
			if matches == 4:
				return cycle_length

	return 0


def main(cap=1000):
	print('capping at %s' % cap)
	best_int = 1
	best_count = 0

	precision = cap * math.log(cap,2) + 100
	print('precision %s digits' % precision)
	fractions = ['1.0'] * 2
	for i in range(2, cap+1):
		fractions.append(decimals(i, precision))
	print('done init fractions')


	for i in range(2,cap):
		cycle_length = get_cycle(i, fractions[i], cap)
		if cycle_length > best_count:
			print('%s cycle length:   %s' % (i, cycle_length))
			best_count = cycle_length
			best_int = i
		if i % 100 == 0:
			print('(100) %s cycle length: %s' % (i, cycle_length))
	
	print('longest cycle has length %s (by 1/%s)' % (best_count, best_int))
		


if __name__ == '__main__':	
	main()	




