
import time

max = 5000

pentagonal_numbers = []
match_check_list = []


def generate_pentagonal_list():
    change0 = 1
    change1 = 4
    for i in range(1, max+1):
        pentagonal_numbers.append(change0)   

        if len(match_check_list) > 0:
            check_value = match_check_list[0]

            if change0 > check_value[0]:
                match_check_list.pop(0)
            elif change0 == check_value[0]:
                diff = check_value[1]
                print("found match: diff == " + str(diff))
                return
        
        for j in range(1, i):
            difference = change0 - pentagonal_numbers[j]
            if is_pentagonal(difference):
                sum = change0 + pentagonal_numbers[j]
                potential_key = (sum, difference)
                binary_insert(potential_key)
                 
                                  
                
        change0 += change1
        change1 += 3
        
        

            
def binary_insert(key):
    l = 0
    r = len(match_check_list) - 1
    m = 0
    
    while l <= r:
        m = (l + r) // 2
        
        if match_check_list[m][0] < key[0]:
            l = m + 1
        elif match_check_list[m][0] > key[0]:
            r = m - 1
        elif match_check_list[m][0] == key[0]:
            if match_check_list[m][1] != key[1]:
                match_check_list.insert(m, key)
     
            return 
        
    if len(match_check_list) > 0 and key[0] > match_check_list[m][0]:
        m += 1
        
    match_check_list.insert(m, key)

    
    
def is_pentagonal(n):
    l = 0
    r = len(pentagonal_numbers) - 1
    
    while l <= r:
        m = (l + r) // 2
                
        if pentagonal_numbers[m] < n:
            l = m + 1
        elif pentagonal_numbers[m] > n:
            r = m - 1
        elif pentagonal_numbers[m] == n:
            return True
        

        
    return False

def timestamp():
    return time.time()


def main():
    start = timestamp()
    
    generate_pentagonal_list()

    end = timestamp()
    print("total time seconds: " + str(end-start))

if __name__ == "__main__":
    main()
    
    
    
    
    
    