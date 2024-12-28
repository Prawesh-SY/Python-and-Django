class Area:

    def __init__(self,length=None,breadth=None,radius=None):
        self.length=length
        self.breadth=breadth
        self.radius=radius


        #self is must to pass in the parameter in case of creating a method in python 
    def square(self,length):
        return length*length
         #pass is created when the method is empty as a placeholder
    def rectangle(self,length=1,breadth=1):
        return length*breadth
    def circle(self,radius):
        return (3.14)*radius*radius

unish = Area()
    
displayMessage="""
    !!! WELCOME USER !!!
Please choose an option below:
1. Find the area of square
2. Find the area of rectangle
3. Find the area of circle
"""
print(displayMessage)
option = input("User Input: ")
if option == "1":
    length=input("Enter the length of the square: ")
    a=unish.square(float(length))
    print(a)
elif option == "2":
    length=input("Enter the length of the rectangle: ")
    breadth = input("Enter the breadth of the rectangle: ")
    b=unish.rectangle(float(length),float(breadth))
    print(b)
elif option == '3':
    radius=input("Enter the radius of the circle: ")
    c=unish.circle(float(radius))
    print(c)

unish = Area()
