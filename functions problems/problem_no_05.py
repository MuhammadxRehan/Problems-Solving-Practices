# Write a python function which converts inches to cms.
def inches_to_cms(inches):
    return inches*2.4
inches = int(float(input("Enter inches: ")))
print( inches_to_cms(inches))