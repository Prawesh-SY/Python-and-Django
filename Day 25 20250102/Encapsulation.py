class Animal:
    def __init__(self):
        self._type = "Unknown"
        
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self._type = "Dog"
        
dog = Dog()
print(dog._type)

class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"
        self._protected_attribute = "I am protected"
        self.__private_attribute = "I am private"
    
    def public_method(self):
        return "This is a public method"
    
    def _protected_method(self):
        return "This is a protected method"
    
    def __private_method(self):
        return "This is a private method"
    
    def access_private(self):
        return self.__private_method()  # Accessible within the class
    
class SubClass(MyClass):
    def access_protected(self):
        return self._protected_attribute  # Accessible within subclass
    

obj = MyClass()
print(obj.public_attribute)  # Accessible
print(obj.public_method())   # Accessible

objSubClass = SubClass()
print(objSubClass.access_protected())  # Accessible within subclass

print(obj.access_private())  # Accessible within the class
# print(obj.__private_attribute)  # Raises AttributeError



