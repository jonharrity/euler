

path = "/home/jon/Downloads/p042_words.txt"

file = open(path, 'r')
big_string = file.read()


word_list = big_string.split(",")

    
for i in range(len(word_list)):
    word_list[i] = word_list[i][1:-1]
    
print(str(word_list))
print("words: %s " % ( len(word_list)))

from triangle import Triangle
tri = Triangle(3000)


largest_sum = 1


def word_sum(word):
    sum = 0
    for c in word:
        sum += ord(c) - 64
        
    global largest_sum
    
    if sum > largest_sum:
#         print("largest sum update from %s to %s" % (largest_sum, sum))
        largest_sum = sum
    return sum

def is_triangle_word(word):
    sum = word_sum(word)
    return tri.is_triangle[sum]
#     global tri
#     return sum in tri.triangle_numbers


# print("'A' value is %s and should be 1" % (word_sum("A")))
# print("sum of SKY is %s and should be 55" % (word_sum("SKY")))
# print("sum of %s is %s" % ("banana", word_sum("a")))
# print("ord of s is %s but should be 19" % (ord('s') - 96))
print("'A' is a triangle word? %s" % (is_triangle_word('A')))






count = 0
for s in word_list:
    if is_triangle_word(s):
        count += 1

        
        
print("found %s triangle words" % (count))

print("largest sum is %s " % (largest_sum))