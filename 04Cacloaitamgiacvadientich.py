import sys
import stdio
import math
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
if a <= 0 or b <= 0 or c<=0 or (a+b) <= c or (b+c)<=a or (c+a)<=b:
	stdio.writeln('Khong ton tai tam giac day. ') 
else:
	if a==b and b==c:
		stdio.writeln('Tam giac deu')
	else:
		if a==b or b==c or c==a:
			stdio.writeln('Tam giac can')
		else:
			if ((a*a + b*b == c*c)  or (b*b + c*c == a*a) or(c*c + a*a == b*b)):
				stdio.writeln('Tam giac vuong')
			else:
				stdio.writeln('Tam giac thuong')
	p=(a+b+c)/2
	s=math.sqrt(p*(p-a)*(p-b)*(p-c))
	stdio.writeln('Dien tich tam giac la: ' + str(s))
