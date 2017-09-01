
                    
                    
                    
def str_without(string, char):
    result = ""
    once = False
    for s in string:
        if not char in s:
            if not once:
                result += s
                once = True
            
    return result





for i in range(1, 100):
    for j in range(1, 100):
        if (i/j <= 0) or (i/j >= 1):
            None
        else:
            s_num = (s for s in str(i))
            s_den = (s for s in str(j))

            
            for s in s_num:
                if s in s_den:
                    num = str_without(s_num, s)
                    den = str_without(s_den, s)

                    if num == '' or den == '':
                        None
#                     elif num == '0' or den == '0':
#                         None
                    elif not ((int(num)/int(den)) == i/j):
                        None
                    else:   
                        print("%s/%s : %s/%s" % (i, j, num, den))
                    print("%s/%s : %s/%s" % (i, j, num, den))
