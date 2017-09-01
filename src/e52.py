



def contains_same_digits(n):
    for i in range(2, 7):
        if not is_permutation(n, i*n):
            return False
    return True

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


        
import time
time_start = time.time()


if __name__ == "__main__":  
    n = 10
    while 1:
        c = str(n)
        
        if c[0] == "1" and contains_same_digits(n):
            print("works for %s" % n)
            break
            
        
        n += 1
    

                    
                    
    time_end = time.time()
    time_diff = time_end - time_start
    
    print("time sec: %f" % time_diff)
    
    
    
    