# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

words = {
    "kela": "banana",
    "saaib": "apple",
    "malta":"oriange"
}
word = input("Enter a word: ")
# method 1
print(words[word])


# method 2
meaning = words.get(word)
print(meaning)


# method 3 
meaning = words.get(word)
if meaning:
    print("meaning is", meaning)
else:
    print("Word not found..!")


