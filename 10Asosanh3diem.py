import sys
import stdio
import math
Xa=float(sys.argv[1])
Ya=float(sys.argv[2])
Xb=float(sys.argv[3])
Yb=float(sys.argv[4])
Xc=float(sys.argv[5])
Yc=float(sys.argv[6])
kc1=math.sqrt(Xa*Xa + Ya*Ya)
kc2=math.sqrt(Xb*Xb + Yb*Yb)
kc3=math.sqrt(Xc*Xc + Yc*Yc)
max=kc1
if kc2 > max:
	max=kc2
if kc3 > max:
	max=kc3
if max == kc1:
	stdio.writeln('Diem 1 xa goc toa do nhat')
if max == kc2:
	stdio.writeln('Diem 2 xa goc toa do nhat')
if max == kc3:
	stdio.writeln('Diem 3 xa goc toa do nhat')







