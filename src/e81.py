




data = None

with open('e81_matrix', 'r') as stream:
    data = list(row.split(',') for row in stream.read().split('\n'))


# for column_start in range(80):
#     row = 79
#     column = column_start
#     
#     while 1 <= row <= 79 and 1 <= column <= 79:
#         if data[row-1][column] < data[row][column-1]:
#             data[row-1][column] = data[row][column]
#             row -= 1
#         else:
#             
#               

minimum_sum = 999*80

for column in range(80):
    sum = 0
    
    try:
        while 0 <= row <= 79 and 0 <= column <= 79:
            sum += data[row][column]
            if data[row-1][column] < data[row][column-1]:
    except: 