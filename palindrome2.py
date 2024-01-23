fh=open('palindrome2.txt','w')
string=input("enter the value:")
reverse=string[::-1]
if(reverse==string):
    fh.write(str("palindrome"))
else:
    fh.write(str(" Not palindrome"))

    

