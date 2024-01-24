#number and decimal to binary
fh=open('Baseno.txt','w')
a=input("enter binary number:")
from_base=2
answer=int(a,from_base)
fh.write(str(answer))
fh.write('\n')
b=int(input("enter the decimal:"))
answer=bin(b)
fh.write(str(answer[2:]))
fh.close()
