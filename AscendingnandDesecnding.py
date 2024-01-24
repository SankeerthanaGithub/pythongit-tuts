fh=open('AscendingandDescending.txt','w')
a=[45,6,7,34,67]
fh.write(str('Before ascending sort\n'))
fh.write(str(a))
fh.write(str('\n'))
fh.write(str('After  ascending sort & desecnding sort\n'))
a.sort()
fh.write(str(a))
a.sort(reverse=True)
fh.close()


