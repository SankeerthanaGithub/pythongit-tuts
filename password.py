fh=open('password.txt','w')
import random
length=8
password=''
password_list='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
i=1
while(i<=length):
    password=password+random.choice(password_list)
    i=i+1
fh.write(password)
