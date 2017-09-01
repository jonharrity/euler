

import time


def main():
    
    sample_space = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    five_p_nine = []
    
    count = 0
    
    for i in range(1, 10):
        for j in range(1, 10):
            if j == i:
                continue
            for k in range(1, 10):
                if k == i or k == j:
                    continue
                for l in range(1, 10):
                    if l == i or l == j or l == k:
                        continue
                    for m in range(1, 10):
                        if m == i or m == j or m == l or m == k:
                            continue
                        
                        five_p_nine.append([i, j, k, l, m])
                        count += 1


    assert count == 15120
    
    pandigital_products = []
    
    for mult in five_p_nine:

        product = (mult[0]*10 + mult[1]) * (mult[2]*100 + mult[3]*10 + mult[4])
        if product > 9999 or product < 1000:
            continue

        product_arr = get_digits(product, [])[::-1]
        mult.extend(product_arr)
        if is_pandigital(mult):
            print("pandigital product: %a" % product)
            if not product in pandigital_products:
                pandigital_products.append(product)
                  
                  
                  
                  
    for mult2 in five_p_nine:
        
        product = (mult2[0]) * (mult2[1]*1000 + mult2[2]*100 + mult2[3]*10 + mult2[4])
        if product > 9999 or product < 1000:
            continue
          
        product_arr = get_digits(product, [])[::-1]
        mult2.extend(product_arr)
        if is_pandigital(mult2):
            print("pandigital product: %a" % product)
            if not product in pandigital_products:
                pandigital_products.append(product)
                  
                       
    
    
    sum = 0
    for i in pandigital_products:
        sum += i
        
    print("ans: " + str(sum))

        
    
    
def get_digits(n, arr):
    if n < 10:
        arr.append(n)
        return arr
    else:
        mod = n % 10
        n = int(n/10)
        arr.append(mod)
        return get_digits(n, arr)
    
    
    
    
def is_pandigital(digits):
    if len(digits) != 9:
        return False
    
    for i in range(1, 10):
        if not i in digits:
            return False
        
    return True

    
    





if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    
    print("total time seconds: " + str(end - start))