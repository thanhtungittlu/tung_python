import stdio
n=stdio.readInt()
s=''
while n//2 > 0:
    s=s+str(n%2)
    n=n//2
s=s+'1'
kq=''
i=len(s)-1
while i>=0:
    kq=kq+s[i]
    i=i-1
stdio.writeln(kq)