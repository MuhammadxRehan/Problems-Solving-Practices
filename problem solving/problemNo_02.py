# Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
# method 1 
# dis_set = set()
# no1 = int(input("Enter a number:"))
# dis_set.add(no1)
# no2 = int(input("Enter a number:"))
# dis_set.add(no2)
# no3 = int(input("Enter a number:"))
# dis_set.add(no3)
# no4 = int(input("Enter a number:"))
# dis_set.add(no4)
# no5 = int(input("Enter a number:"))
# dis_set.add(no5)
# no6 = int(input("Enter a number:"))
# dis_set.add(no6)
# no7 = int(input("Enter a number:"))
# dis_set.add(no7)
# no8 = int(input("Enter a number:"))
# dis_set.add(no8)
# print(dis_set)

# method 2 
main_set = set()
for i in range(8):
    num = int(input("Enter a number:"))
    main_set.add(num)
print(main_set)
