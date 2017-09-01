




def is_valid(n):
    s = str(n)
    
    if not len(s) == 19:
        return False
    
    if not s[len(s)-1] == '0':
        return False
    
    for i in range(1, 10):
        if not s[(i-1)*2] == str(i):
            return False
        
    return True



def main():
    min = 1010101010
    max = 1389026623




    for i in range(min, max, 10):
        if is_valid(i**2):
            print("valid: %d" % i)


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    stop = time.time()
    total_time = stop-start
    print("total time: %s" % total_time)