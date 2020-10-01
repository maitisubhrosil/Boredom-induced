star = "*"
space = " "
start = 0
inc = 1
inc1 = 0
inc2 = 0
u_inp = int(input("Enter pattern size::"))
end = u_inp
line = ""

for i in range(1,end):
    line = (i*star)+((u_inp-1-i)*space)+" "+((u_inp-i)*star)
    print (line)
    
#print (((end-1)*" ")+"o")   #center design
   
for j in range(end-1,0,-1):
    inc1 = start+inc
    inc2 = inc1
    line = (j*space)+((start+inc)*star)+(inc1*space)+((inc2+j-inc1)*star)
    inc+=1
    u_inp-=1
    print (line)
