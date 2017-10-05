
import math




def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
def strip(s, char):
    loc = s.find(char)
    s = s[0:loc] + s[loc+1:]
    return s

def get_reduced(num, den):
    if num < 10:
        return
    
    snum = str(num)
    sden = str(den)
    inter = set(snum).intersection(set(sden))
    if len(inter) < 1:
        return None
    else:
        val = inter.pop()
        num = int(strip(snum, val))
        den = int(strip(sden, val))
        if val == '0' or num == 0 or den == 0 or num >= den:
            return None
        return (num, den)

def fractions_equal(f1, f2):
    return abs(f1[0]/f1[1] - f2[0]/f2[1]) < .001

def simplified(num, den):
    g = gcd(num, den)
    return (round(num/g), round(den/g))




def alg2():
    
    
    limit = 100
    
    solnum = 1
    solden = 1
    
    for den in range(2, limit):
        for num in range(1, den):
            reduced = get_reduced(num, den)
#             if reduced:
#                 print('%s/%s reduced is %s/%s' % (num,den,reduced[0],reduced[1]))
            if reduced and fractions_equal((num, den), reduced):
                result = simplified(num, den)
                solnum *= result[0]
                solden *= result[1]
#                 print('%s/%s -> %s/%s' % (num,den,result[0],result[1]))
#                 print(reduced)
    result = simplified(solnum, solden)
#     print('%s/%s -> %s/%s' % (solnum, solden, result[0], result[1]))
    print(result[1])



if __name__ == '__main__':
    import metric
    metric.Metric(alg2)
    
    
    
    
    
    
    
    