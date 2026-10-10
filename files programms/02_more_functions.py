file = open("namefile.txt")
# line  =file.readlines()
# print(line, type(line))

# file.close


lines = file.readline()
while(lines != ""):
    print(lines)
    lines = file.readline()
file.close
