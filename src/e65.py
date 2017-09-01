def get_pattern():
    yield 0
    
    k = 1
    while 1:
        yield 1
        yield 2*k
        yield 1
        k += 1


base = 2
simple_n_im1 = 1
d_im1 = 1


simple_n_im2 = 0
d_im2 = 1


pattern_generator = get_pattern()
pattern_generator.send(None)
pattern_generator.send(None)


i = 1
for i in range(3, 101):
    pattern = pattern_generator.send(None)
    
    simple_n = simple_n_im1 * pattern + simple_n_im2
    d = d_im1 * pattern + d_im2
    
    
    if i==100:
        n = simple_n + base*d
        print(sum(int(j) for j in str(n)))
    
    simple_n_im2 = simple_n_im1
    simple_n_im1 = simple_n
    d_im2 = d_im1
    d_im1 = d
    






