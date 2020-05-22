import sys
import math

def is_dec_pal(x):#is x where type(x)==type(1) a palindrome?
	s = str(x)
	lmid = len(s)//2
	hmid = math.ceil(len(s)/2)
	return s[:lmid] == s[hmid:][::-1]
	

def get_pals_to_len(x):#return list of binary palindromes up to string length x

	cache = {0: [''], 1: ['0','1']}

	def _(x):
		if x in cache:
			return cache[x]
		else:
			prev = _(x-2)
			newitem = ['0'+s+'0' for s in prev] + ['1'+s+'1' for s in prev]
			cache[x] = newitem
			return cache[x]

	
	_(x)
	ans = []
	for i in range(1,x+1):
		ans += _(i)
	return ans

def get_double_pals(cap):
	binpals = get_pals_to_len(math.ceil(math.log(cap,2)))

	dpals = set()	
	for bs in binpals:
		if bs[0] == '0':
			continue
		dec = int(bs, 2)
		if dec > cap:
			break
		if is_dec_pal(dec):
			if not dec in dpals:
				print('%s = %s' % (bs,str(dec)))
			dpals.add(dec)
	ans = sum(x for x in dpals)
	print('sum %s' % ans)
	return ans

if __name__ == '__main__':
	cap = int(sys.argv[1])
	print(get_double_pals(cap))
