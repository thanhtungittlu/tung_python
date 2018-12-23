import sys
import stdio
a=int(sys.argv[1])
k=1
while k <= a:
	for i in range(1,k+1):
		stdio.write(' ')
	for i in range(k,a+1):
		stdio.write('*')
	k=k+1
	stdio.writeln()

#Minh hoa: 
# *****
#  ****
#   ***
#    **
#     *

