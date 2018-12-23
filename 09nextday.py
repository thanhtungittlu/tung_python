import sys
import stdio
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
if (a<1 or a>31) or ( b<1 or b>12) or ( c<1 ) or ( b ==2 and  a > 29 ) or ( ((b==4)or(b==6)or(b==9)or(b==11))and a == 31 ) or ( b==2 and a==29 and ( (c%4 !=0 or c%100==0) and c % 400 !=0 ) ):
	stdio.writeln('Du lieu nhap sai! ')
# Nếu ngày lớn hơn 31 hoặc tháng lớn hơn hoặc tháng 4,6,9,11 có ngày 31 hoặc thang 2 của nhưng năm không nhuận có 29 ngày thì in ra màn hình là dữ liệu nhập sai.  
else:
	if ( a==31 and b==12 ):
		a1 = 1
		b1 = 1
		c1 = c+1
	else:
		if ( ((b==1 or b==3 or b==5  or b==7 or b==8 or b==10 ) and a==31) or ((b==4 or b==6 or b==9 or b==11) and a==30) or ( b==2 and ( ( c%4 == 0 and c % 100 != 0 ) or c % 400 == 0 ) and a==29) or ( b==2 and a==28 and ( (c%4 !=0 or c%100==0) and c % 400 !=0 ) )):
			a1 = 1
			b1 = b+1 
			c1 = c
#Nếu tháng 1,3,5,7,8,10 và đang là ngày 31 hoặc tháng 4,6,9,11 đang là ngày 30 hoặc nhưng năm nhuận tháng 2 đang 29 ngày hoặc những năm không nhuận tháng 2 có 28 ngày thì sẽ sang tháng mới
		else:
			if b==2 and ((c % 4 == 0 and c % 100 != 0) or c%400 == 0) and a==28:
				a1 = 29
				b1 = b
				c1 = c
#Ngày 28 tháng 2 của năm nhuận thì tiếp theo sẽ là ngày 29 tháng 2
			else:
				
				a1=a+1
				b1=b
				c1=c

	stdio.writeln('Tiep theo la Ngay: '+ str(a1) + ' Thang: ' + str(b1) + ' Nam: ' + str(c1) )
			

	
	 
		
		 
