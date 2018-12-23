#Kiem tra xem uoc nao la lon nhat va xem so do co phai so nguyen to khong neu khong phai thi kiem tra uoc tiep theo
import stdio
import math
n=stdio.readInt()
k=int(n/2)+1
while k>=1:
    if n%k==0:
        flag=True
        for i in range(2,int(math.sqrt(k))+1):
            if k % i ==0 :
                flag=False
                break
        if flag==True:
            stdio.writeln(k)
            break
    k=k-1