import sys
import stdio
a=int(sys.argv[1])
b=int(sys.argv[2])
min=a
if b < min:
	min=b
stdio.writeln(min)
