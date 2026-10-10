#  files are used to store data permanently in computer ...
#  commonly our programs are run in Ram which a voltile momery
#  means once our program terminates than Ram memory lost ...
#  to make our programs permantly store in computer we used HHD or SSD
#  once our files store in computer than we can use it in program for 
#  this we used file I/O 


f = open("files.txt")
data = f.read()
print(data)
f.close
