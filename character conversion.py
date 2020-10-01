def pattern_a(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    for i in range(mid,0,-1):
        line = (space*(i))+(star)+(space*(inc*2))+(star)
        inc+=1
        print line 
    print (" "+(star*size))
    for j in range(end/2):
        line = (" "+star)+" "+(space*(size-4))+" "+(star)
        print line 
        
#pattern_a(10)
#print ("\n")
#print ("\n")

def pattern_z(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    print (star*size)
    for i in range(end-1,0,-1):
        line = (space*(i))+(star)
        print line
    print (star*size)
    
#pattern_z(10)
#print ("\n")
#print ("\n")

def pattern_h(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    for i in range(end/2):
        line = (star)+(space*(size-2))+(star)
        print line 
    print (star*size)
    for j in range(end/2):
        line = (star)+(space*(size-2))+(star)
        print line 
        
#pattern_h(10)
#print("\n")
#print("\n")

def pattern_b(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    print (star*(size-1))
    for i in range(end/3):
        line = (star)+(space*(size-2))+(star)
        print line
    print (star*(size-1))
    for j in range(end/3):
        line = (star)+(space*(size-2))+(star)
        print line 
    print (star*(size-1))
    
#pattern_b(10)
#print("\n")
#print("\n")

def pattern_r(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    print (star*(size-1))
    for i in range(end/3):
        line = (star)+(space*(size-2))+(star)
        print line
    print (star*(size-1))
    for j in range(end/2):
        line = (star)+(space*(inc*2))+(star)
        inc+=1
        print line
        
#pattern_r(10)
#print("\n")
#print("\n")

def pattern_t(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    print (star*(size))
    for i in range(end-1):
        line = (space*mid)+(star)
        print line
    
#pattern_t(11)
#print("\n")
#print("\n")

def pattern_m(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    inc1 = 0
    inc2 = 0
    for i in range(end):
        inc1 = start+inc
        inc2 = inc
        line = (star)+(space*(i))+(star)+(space*(end-i-1)*2)+(star)+(space*(i))+(star)
        inc+=1
        print line
        
#pattern_m(10)
#print("\n")
#print("\n")

def pattern_e(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    inc1 = 0
    inc2 = 0
    print (star*(end-1))
    for i in range(end/3):
        line = (star)
        print (line)
    print (star*(end-1))
    for i in range(end/3):
        line = (star)
        print (line)
    print (star*(end-1))

#pattern_e(10)
#print("\n")
#print("\n")

def pattern_i(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    inc1 = 0
    inc2 = 0
    for i in range(size):
        line = (space*5)+(star)
        print line

#pattern_i(10)
#print("\n")
#print("\n")

def pattern_l(size):
    star = "*"
    space = " "
    line = ""
    start = 0
    end = size
    mid = end//2
    inc = 0
    inc1 = 0
    inc2 = 0
    for i in range(size):
        line = (space*3)+(star)
        print line
    print ((space*3)+(star*(size)))

#pattern_l(10)
#print("\n")
#print("\n")


pattern_h(10), pattern_i(10), pattern_t(10), pattern_l(10), pattern_e(10), pattern_r(10)
