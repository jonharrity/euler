from itertools import permutations

ngon = 5



    
def get_all_sets(total):
    all = []
    for i in range(1, 2*ngon+1):
        for n in gen2more(total, i):
            all.append(n)
    return all

def get_all_filtered_sets(total):
    sets = get_all_sets(total)
    rm = set()
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            repeat = 0
            for x in sets[i]:
                if x in sets[j]:
                    repeat += 1
            if repeat > 1:
                rm.add(j)
    total_removed = 0
    for i in rm:
        sets.pop(i-total_removed)
        total_removed += 1
    return sets


def sorted_5permutation(data):
    perms = []
    size = len(data)
    for i in range(1, size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                for l in range(k+1, size):
                    for m in range(l+1, size):
                        perms.append((data[i],data[j],data[k],
                                      data[l],data[m]))
    return perms


def sorted_5permutations_ints():
    perms = []
    for i in range(1, 2*ngon+1):
        for j in range(i+1, 2*ngon+1):
            for k in range(j+1, 2*ngon+1):
                for l in range(k+1, 2*ngon+1):
                    for m in range(l+1, 2*ngon+1):
                        perms.append((i,j,k,
                                      l,m))
    return perms

def filter_sets_by_intersects(filtered_sets):
    intersects = set()
    solution_sets = set()
    for perm in sorted_5permutations_ints():
        for n in sorted_5permutation(filtered_sets):
            count = list(0 for x in range(ngon))#eg, [0,0,0,0,0]
            for i in n:
                for j in i:
                    if j in perm:
                        count[perm.index(j)] += 1
            if count == list(2 for x in range(ngon)):
                intersects.add(perm)
                solution_sets.add(n)
                
    rm = set()
    for solution in solution_sets:
        s = ""
        for i in range(len(solution)):
            for j in solution[i]:
                s += str(j)
        if len(s) != 16:
            rm.add(solution)
            
    solution_sets.difference_update(rm)
                
    return (intersects, list(solution_sets))
        

def gen2more(total, first):
    all = []
    for i in range(1, 2*ngon+1):
        if i != first:
            n = total - first - i
            if n < 1 or n > 2*ngon:
                pass
            elif i != n != first:
                all.append((first, i, n))
    return all

def get_all_solutions(total):
    return list(permutations(get_all_sets(total), ngon))
    
    
    
if __name__ == '__main__':
    for total in range(15, 21):
#     for total in range(15, 16):
        filtered_sets = get_all_filtered_sets(total)
        intersect_data = filter_sets_by_intersects(filtered_sets)
        print("total=%s: %s sets, %s intersects, %s solution sets" % (total, 
            len(filtered_sets),
            len(intersect_data[0]),
            len(intersect_data[1])))
             
    print("solution sets:" )
    max = 0
    for total in range(15, 21):
        filtered_sets = get_all_filtered_sets(total)
        intersect_data = filter_sets_by_intersects(filtered_sets)
        s = ""
        for n in intersect_data[1]:
            solution = ""
            for set_x in n:
                for i in set_x:
                    solution += str(i)
            if int(solution) > max:
                max = int(solution)
            s += solution
            s += ", " 
        print(s)
    print("max: %s" % max)
         
         
        