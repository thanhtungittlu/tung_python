import stdio
n=stdio.readInt()
while n >= 1:
    s=0
    for i in range (1,int(n/2)+1):
        if n % i == 0:
            s=s+i
    if s==n:
        stdio.writeln(n)
        break
    n=n-1