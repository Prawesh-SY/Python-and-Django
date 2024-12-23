# Product
product = lambda num1,num2:num1*num2
print("Product of 3 and 4 =",product(3,4))

square = lambda num: num*num
print("Square of 7 = ",square(7))

# Map
nums=[1,2,3,4,5,6,7,8,9]
sqr = list(map(lambda x: x**2 , nums))
print(f"The square of number present in {nums} is: ",sqr)

cube = list(map(lambda x: x**3, nums))
print(f"The cube of numbers present in {nums} is: ",cube)