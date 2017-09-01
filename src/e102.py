"""The point of origin is inside a triangle if the triangle 
contains both positive and negative x and y intercept.
"""

def contains_origin(triangle):
    intercepts = [0,0,0,0] # x pos, x neg, y pos, y neg
    for i in range(3):
        j = i + 1
        if j == 3:
            j = 0
        line = (triangle[i], triangle[j])
        
        
        x_intercept = get_x_intercept(line)
        y_intercept = get_y_intercept(line)
        
        if x_intercept != None:
            if x_intercept >= 0:
                intercepts[0] = 1
            if x_intercept <= 0:
                intercepts[1] = 1
        if y_intercept != None:
            if y_intercept >= 0:
                intercepts[2] = 1
            if y_intercept <= 0:
                intercepts[3] = 1
        
    return intercepts == [1,1,1,1]


def get_x_intercept(line):
    if line[0][1] < 0 and line[1][1] < 0:
        return None
    if line[0][1] > 0 and line[1][1] > 0:
        return None
    
    m = get_slope(line)
    try:
        x = ( m * line[0][0] - line[0][1] ) / m
    except:#divide by 0
        x = line[0][0]
    return x


def get_y_intercept(line):
    if line[0][0] < 0 and line[1][0] < 0:
        return None
    if line[0][0] > 0 and line[1][0] > 0:
        return None
    
    m = get_slope(line)
    y = m * -1 * line[0][0] + line[0][1]
    
    return y

def get_slope(line):
    dx = line[1][0] - line[0][0]
    dy = line[1][1] - line[0][1]

    try:
        m = dy / dx
    except:#divide by 0
        m = 10 ** 10
        
    return m

def read_triangles():
    file = open("e102_data", 'r')
    while 1:
        line = file.readline()
        if line == "":
            break
        values = line.split(",")
        yield([ [int(values[0]),int(values[1])] , 
                [int(values[2]),int(values[3])] , 
                [int(values[4]),int(values[5])]])
        
    
    file.close()
    


def main():
    count = 0
    total_read = 0
    for triangle in read_triangles():
        if contains_origin(triangle):
            count += 1
        total_read += 1
    assert total_read == 1000
    print(count)
    
    
    
if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print("time sec: %s" % (end-start))
    
    
    
    
    
    
    
    
    