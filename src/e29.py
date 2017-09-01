




list = []

for i in range(2, 101):
    for j in range(2, 101):
            n = i**j
            if not n in list:
                list.append(n)
                
print(len(list))