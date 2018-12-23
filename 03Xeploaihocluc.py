import sys
import stdio
a=float(sys.argv[1])
b=float(sys.argv[2])
c=int(sys.argv[3])
dqt=(10-c)*0.3 + a*0.7
if c > 4 or dqt < 4:
	stdio.writeln('Ban bi cam thi, hen gap lai ky sau! ')
else:
	dtb=dqt*0.3 + b*0.7
	if dtb >= 9:
		stdio.writeln('Ban hoc: Xuat sac ')
	else:
		if dtb >= 8:
			stdio.writeln('Ban hoc: Gioi')
		else:
			if dtb >=6.5:
				stdio.writeln('Ban hoc: Kha')
			else:
				if dtb >= 4:
					stdio.writeln('Ban hoc: Trung binh')
				else:
					stdio.writeln('Ban hoc: Kem')


