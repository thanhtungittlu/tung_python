import stdio
import math
n=stdio.readInt()
dem=0
i=2
while dem != n:
    flag=True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j ==0:
            flag=False
            break
    if flag==True:
        dem=dem+1
    i=i+1
stdio.writeln(i-1)