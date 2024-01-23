fh=open('rectangle.txt','w')
l=int(input('enter the length of reactangle:'))
b=int(input('enter the breadth of reactangle:'))
a=l*b
p=2*(l+b)
fh.write(str(a))
fh.write('\n')
fh.write(str(p))
