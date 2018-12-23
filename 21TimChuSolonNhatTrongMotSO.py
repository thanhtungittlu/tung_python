import stdio
n=stdio.readInt()
xau=str(n) #dua ve dang xau
d=len(xau) #do dai cua xau
if d!= 4:
    stdio.writeln(-1)
else:
    max=xau[0]
    for i in range(1,d):
        if xau[i] > max:
            max=xau[i]
    stdio.writeln(max)
        