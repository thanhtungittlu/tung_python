import sys
import stdio
a=int(sys.argv[1])
b=int(sys.argv[2])
if a<1 or a>12:
	stdio.writeln('Khong co thang yeu cau')
else:
		if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
 				stdio.writeln('Thang nay co 31 ngay')
		else:
			if a==4 or a==6 or a==9 or a==11:
				stdio.writeln('Thang nay co 30 ngay') 
			else:
				if ( (b % 4 == 0 and b % 100!=0 ) or (b % 400 == 0) and a==2) :
					stdio.writeln('Thang nay co 29 ngay')
				else:
					stdio.writeln('Thang nay co 28 ngay')
