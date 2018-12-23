import sys
import stdio
a=int(sys.argv[1])
k=a
while k > 0:
	for i in range(1,k+1):
		stdio.write('*')
	k=k-1
	stdio.writeln()

# Minh hoa: 7
# *******
# ******
# *****
# ****
# ***
# **
# *

#Cach 2
#import sys
#import stdio
#a=int(sys.argv[1])
#k=1
#while k <= a:
#	for i in range(1,a-k+2):
#		stdio.write('*')
#	for i in range(1,k):
#		stdio.write(' ')	
#	k=k+1
#	stdio.writeln() 
		



