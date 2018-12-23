import sys
import stdio
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
min=a
if b < min:
	min=b
if c < min:
	min=c
stdio.writeln(min)

