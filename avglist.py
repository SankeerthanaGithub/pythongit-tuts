fh=open('avg of list.txt','w')
abc=[1,2,3,4,5,6,7,8,9]
sum=0
i=0
while(i<len(abc)):
    sum=sum+abc[i]
    i=i+1
avg=int(sum/len(abc))
fh.write(str('the average is:'))
fh.write(str(avg))