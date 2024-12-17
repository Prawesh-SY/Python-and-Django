# WAP to swap data in to varibles:

a=5
b=9

print("Before swap a= ", a)
print("Before swap b= ", b)

# Failed attempt
# a=a+b-a
# b = a+b-b

# Using temp variable c
# c=a
# a=b
# b=c

# Without using temp variable
a,b=b,a

print("After swap a= ", a)
print("After swap b= ", b)




print("Swapping again without ")