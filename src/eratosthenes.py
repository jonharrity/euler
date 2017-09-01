'''
Created on Jun 24, 2016

@author: jon
'''

class Eratosthenes():
    


    def __init__(self, max):
        self.isPrime = []
        for i in range(max+1):
            self.isPrime.append(True)
            
        self.isPrime[:2] = [False, False]
        self.primes = None
        
        n = 2
        while n < max:
            if self.isPrime[n]:
                for i in range(n+n, max, n):
                    self.isPrime[i] = False
            n += 1
                
                
      
    def get_primes(self):
        if self.primes == None:
            self.primes = []
            for i in range(len(self.isPrime)):
                if self.isPrime[i]:
                    self.primes.append(i)
                    
        return self.primes
                
if __name__ == "__main__":
    print(Eratosthenes(20).isPrime)