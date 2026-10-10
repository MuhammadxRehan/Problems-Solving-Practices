#  A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comt = input("Enter you comment:")

if(p1 in comt or p2 in comt or p3 in comt or p4 in comt ):
    print("This comment is a spam.")
else:
    print("This comment is not a spam.")