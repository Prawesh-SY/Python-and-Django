# class BaseClass:
#     pass
# class DerivedClass(BaseClass):
#     pass

class Person:
    
    def __init__(self, gender="male"):
        self.gender = gender
        pass
    def getGender(self):
        print(f"I am {self.gender}")
        
class Student(Person):
    def  __init__(self, name):
        self.name = name
        Person.__init__(self)
        # super.__init__()
        pass
    def study(self):
        print(f"My name is {self.name} and I am studying in Vrit Tech")
        
ramObj = Student("Ram")
ramObj.study()
ramObj.getGender()
print(ramObj.gender)
