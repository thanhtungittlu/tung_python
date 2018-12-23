import stdio
n=stdio.readInt()
while n >= 2:
    flag=True
    for i in range (2,n):
        if n % i == 0:
            flag=False
            break
    if flag==True:
        stdio.writeln(n)
        break
    n=n-1