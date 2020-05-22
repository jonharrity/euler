import sys
import math
from itertools import combinations


def tadd(t, s):#destructive, adds s to t (a trie)
	if s == '':
		t[1] = True
		return 
	if not s[0] in t[0]:
		t[0][s[0]] = [{}, False]
	tadd(t[0][s[0]], s[1:])

def tcount(t, s):#count s in t, can use * in s
	if len(s) == 0:
		return t[1]
	
	
	if s[0] == '*':
		return sum(tcount(t[0][x], s[1:]) for x in t[0].keys())
	else:
		return tcount(t[0][s[0]], s[1:]) if s[0] in t[0] else 0


def genprimes(cap):
	isprime = [False,False] + [True]*(cap-1)
	i = 2
	primes = []
	while i < cap:
		primes.append(i)
		for j in range(i*2, cap+1, i):
			isprime[j] = False	
		i += 1
		while i < cap and not isprime[i]:
			i += 1
	return primes

def addstars(s, x):
    if len(str(s)) < x:
        raise Exception('cannot add %s stars to %s' % (str(x), s))

    l = []
    for arrangement in combinations(range(len(s)), x):
        news = s
        for i in arrangement:
            news = news[:i] + '*' + news[i+1:]
        l.append(news) 
    return l 

def addincstars(s, x):
    l = []
    for i in range(1, x+1):
        l.extend(addstars(s, i))
    return l

def findfamily(minprime, maxprime, maxfamilysize):
    primes = genprimes(maxprime)
    primes = [str(x) for x in filter(lambda x: x>minprime, primes)]
    tri = [{}, False]
    for prime in primes:
        tadd(tri, prime)
     
    for familysize in range(5, maxfamilysize):
        for prime in primes:
            queries = addincstars(prime, 2)
            for query in queries:
                foundsize = tcount(tri, query) 
                if foundsize >= familysize:
                    print('found family size of %s from prime %s' % (foundsize, prime))
                    break
        
          


def family_size(slen):
	min_x = 10**(slen-1)
	max_x = min_x * 10 - 1
	primes = genprimes(max_x)
	primes = [str(x) for x in filter(lambda x: x>=min_x, primes)]
	print('using primes %s' % primes)

	tri = [{},False]
	for prime in primes:
		tadd(tri, prime)
	print(tcount(tri, '*'))
	print(tcount(tri, '*7'))
	



if __name__ == '__main__':
    findfamily(10**4, 10**5-1, 7)
    quit()
    primes = genprimes(10**6)
    tri = [{},False]
    for prime in primes:
	    tadd(tri, prime)
    print(tcount(tri, '*'))
	
