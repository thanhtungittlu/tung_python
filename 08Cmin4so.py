import sys
import stdio
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
d=int(sys.argv[4])
min=a
if b < min:
	min=b
if c < min:
	min=c
if d < min:
	min=d
stdio.writeln(min)

