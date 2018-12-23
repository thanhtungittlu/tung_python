import stdio
n=stdio.readInt()
xau=str(n) #dua ve dang xau
d=len(xau) #Tao xau rong
if d != 4:
    stdio.writeln(-1)
else:
    xr=str()
    i=d-1
    while i>=0:
        xr=xr+xau[i]
        i=i-1
    if xr==xau:#Kiem tra coi 2 xau nay co bang nhau khong
        stdio.writeln('DX')
    else:
        stdio.writeln('KDX')
        
