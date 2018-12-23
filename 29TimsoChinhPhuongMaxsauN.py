import stdio
import math
n=stdio.readInt()
while n>=1:
    flag=False
    for i in range(1,int(math.sqrt(n))+1):
        if n==i*i:
            flag=True
            break
    if flag==True:
        stdio.writeln(n)
        break
    n=n-1