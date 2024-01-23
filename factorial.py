
fh=open('factorial.txt','w')
num=int(input("enter the number:")) #dynamic way
sum=1
i=1
while(i<=num):
    sum=sum*i
    i=i+1
fh.write(str(sum))
fh.write('\n')
fh.close()

#static way
'''fh=open('factorial.txt','w')
sum=1 
i=1
n=8
while(i<=n):
    sum=sum*i
    i=i+1
fh.write(str(sum))
fh.write('\n')
fh.close() '''

