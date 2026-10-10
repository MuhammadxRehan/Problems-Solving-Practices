# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with R. 
names = ["Rehan", "Hammad", "Aoun" , "Roshan"]
 
for i in names:
    if(i.startswith("R")):
        print(f"Assalam o alikum {i}!")
        