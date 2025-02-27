# class Shape:
#     def __init__(self,name):
#         self.name = name
    
#     def area(self):
#         pass
    
#     def fact(self):
#         return "I am a 2D shape."
    
#     def __str__(self):
#         return self.name
        
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length
        
#     def area(self):
#         return self.length**2
    
#     def fact(self):
#         return "Square have each angle to 90 degree"

class Animal:
    def __init__(self):
        pass
    def sound(self):
        print("Difficult to predict")
        
class Cat(Animal):
    def work(self):
        print("I climb curtains")
        
    def sound(self):
        print("Mewo Mewo")
    pass

luna = Cat()
luna.work()
luna.sound()

another_animal = Animal()
# another_animal.work()
another_animal.sound()