# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
# for entering marks 
sub1 = int(input("Enter your marks:"))
sub2 = int(input("Enter your marks:"))
sub3 = int(input("Enter your marks:"))

if(sub1<0 or sub1 >100 or sub2<0 or sub2>100 or sub3>100 or sub3<0 ):
    print("Invalid marks")
else:

    # total percentag 
    total_pt =(((sub1 + sub2 +sub3)/300)*100)
    #  main conditions
    if(total_pt >= 40 and sub1>=33 and sub2>= 33 and sub3>33 ):
        print("you passed!")
    else:
        print("you failed!")

