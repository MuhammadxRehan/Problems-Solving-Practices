# Write a python program using function to convert Celsius to Fahrenheit. 
# we knew that c = 5/9(f-32) 

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter tem in F :"))

print(f_to_c(f))

# f= 9/5(c+32)

def c_to_f(c):
    return 9*(c+32)/5

c = int(input("Enter tem in C :"))

print(c_to_f(c))

