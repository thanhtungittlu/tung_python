import stdio
a=stdio.readFloat()
b=stdio.readFloat()
c=stdio.readFloat()
d=stdio.readFloat()
DTB=( (a+c)*2 + b + d )/6
if DTB >=9: 
    if a > 6.5 and b > 6.5 and c > 6.5 and d > 6.5:
        stdio.writeln('XS')
    else:
        stdio.writeln('G')
else:
    if DTB >=8:
        if a > 5 and b > 5 and c > 5 and d > 5:
            stdio.writeln('G')
        else:
            stdio.writeln('K')
    else:
        if DTB >=6.5:
            if a > 3 and b > 3 and c > 3 and d > 3:
                stdio.writeln('K')
            else:
                stdio.writeln('TB')
        else:
            if DTB >=5:
                if a > 2 and b > 2 and c > 2 and d > 2:
                    stdio.writeln('TB')
                else:
                    stdio.writeln('Y')
            else:
                 stdio.writeln('Y')
        