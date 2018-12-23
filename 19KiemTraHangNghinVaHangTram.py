import stdio
n=stdio.readInt()
xau=str(n) #Chuyen ve ham ky tu
d=len(xau) #Do dai cua xau
if d==2 or d == 1:
    stdio.writeln(00)
else:
    if d==3:
        stdio.writeln( '0' + xau[2])
    else:
        stdio.writeln(xau[d-4] + xau[d-3])
    
