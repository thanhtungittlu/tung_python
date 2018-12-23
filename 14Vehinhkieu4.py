import sys
import stdio
a=int(sys.argv[1])
k=1
while k <= a:
	for i in range(1,a-k+1):
		stdio.write(' ')
	for i in range(a-k,a):
		stdio.write('*')
	k=k+1
	stdio.writeln()

#Minh hoa: 6
#      *
#     **
#    ***
#   ****
#  *****
# ******
		
