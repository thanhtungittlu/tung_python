#Chuong trinh tinh tong S= 1 + 1*2 +1*2*3 + ... + 1*2*3*..*n 
import stdio
stdio.write('Nhap n tu ban phim: ')
n=stdio.readInt()
s=0
for i in range(1,n+1):
	c=1
	for j in range (1,i+1):
		c=c*j
	s=s+c
stdio.writeln('Ket qua: ' +str(s))
