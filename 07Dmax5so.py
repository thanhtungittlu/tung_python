import sys
import stdio
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
d=int(sys.argv[4])
e=int(sys.argv[5])
max=a
if b > max:
	max=b
if c > max:
	max=c
if d > max:
	max=d
if e > max:
	max=e
stdio.writeln(max)

