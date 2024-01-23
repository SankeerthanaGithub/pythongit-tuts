fh=open('leapyear.txt','w')
year=int(input('enter the year:'))
if(year%100!=0)&(year%4==0):
    fh.write('This is leap year')
else:
    fh.write('This is not leap year')
fh.close()