import stdio
n=stdio.readInt()
if ( n % 4 == 0 and n % 100 != 0 ) or (n % 400 ==0):
    stdio.writeln('Day la nam nhuan')
else:
    stdio.writeln('Day la nam khong nhuan')
    