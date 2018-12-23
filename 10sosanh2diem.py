import sys
import stdio
import math
Xa=float(sys.argv[1])
Ya=float(sys.argv[2])
Xb=float(sys.argv[3])
Yb=float(sys.argv[4])
kc1=math.sqrt(Xa*Xa + Ya*Ya)
kc2=math.sqrt(Xb*Xb + Yb*Yb)
if kc1 > kc2:
	stdio.writeln ('Diem 1 xa goc toa do hon')
if kc1 < kc2:
	stdio.writeln ('Diem 2 xa goc toa do hon')
if kc1 == kc2:
	stdio.writeln ('2 diem khoang cach nhu nhau')
