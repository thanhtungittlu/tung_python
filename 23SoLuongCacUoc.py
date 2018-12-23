import stdio
n=stdio.readInt()
dem=0
for i in range(1,int(n/2)+1):
    if n % i == 0:
        dem=dem+1
stdio.writeln(dem)