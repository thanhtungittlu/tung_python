import stdio
import math
n=stdio.readInt()
flag=True
for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
        flag=False
        break
if flag==True:
    stdio.writeln('Day la so nguyen to')
else:
    stdio.writeln('Day khong la so nguyen to')
