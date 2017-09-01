

with open("e89_data", 'r') as file:
    arr = file.read().split("\n")
    
    

def arr_in(a, b):
    return "".join(str(i) for i in a) in "".join(str(i) for i in b)
    


ans = 0


for romnum in arr:
#     dic = {"III": "VII", "IIII": "VI", 
#            "XXXX": "LX", "DDDD: "
    dic = {"VV": "X", "LL": "C", "DD": "M"}
    
    start = len(romnum)
    
    for key in dic.keys():
        if key in romnum: 
            print("in it")
            romnum = romnum.replace(key, dic, 1)
            ans += 1
        else:
            print("%s not in %s" % (key, romnum))
        if key in romnum: 
            romnum = romnum.replace(key, dic, 1)
            ans += 1
        
    end = len(romnum)
    
    if not start == end:
        print("change of ", (end-start))
        
print(ans)