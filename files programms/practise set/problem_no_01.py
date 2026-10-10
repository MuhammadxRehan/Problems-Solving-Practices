# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘company’.

with open("poems.txt") as f:
    content = f.read()
    if ("company" in content):
        print("The word is in file content.")
    else:
        print("The word is not in file content.")