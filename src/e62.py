from e70 import is_permutation


cubes = list(i**3 for i in range(1, 10000))
lengths = [0]
for cube in cubes:
    try:
        lengths[len(str(cube))] += 1
    except:
        lengths.append(1)
        
        
print("highest length calculated is %s" % (len(lengths)+1))
        
        
cubes_sorted = []

n = 0
for i in lengths:
    cubes_sorted.append(cubes[n:n+i])
    n += i
        

for arr in cubes_sorted:
    for i in range(len(arr)):
        perms = [arr[i]]
        for j in range(i+1, len(arr)):
            if is_permutation(arr[i], arr[j]):
                perms.append(arr[j])
        if len(perms) == 5:
            print("perms are %s for lengths %s" % (perms, len(str(arr[0]))))