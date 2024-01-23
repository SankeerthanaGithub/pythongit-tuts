fh=open('tempearture.txt','w')
f=float(input("enter the values of farenheit:"))
c=((f-32)*5/9)
fh.write(str(c))
fh.write('\n')
f=float(input("enter the values of celsius:"))
f=(c*(9/5)+32)
fh.write(str(f))

