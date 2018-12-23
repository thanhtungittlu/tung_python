import sys
import stdio
import math
x=float(sys.argv[1])
y=float(sys.argv[2])
a=float(sys.argv[3])
b=float(sys.argv[4])
r=float(sys.argv[5])
d=math.sqrt((x-a)*(x-a)+(y-b)*(y-b))
if d > r:
	stdio.writeln ('Diem nay nam ngoai duong tron')
else:
	stdio.writeln ('Diem nay nam trong duong tron')
