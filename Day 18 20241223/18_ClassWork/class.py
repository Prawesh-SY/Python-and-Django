class Dog:
    species = "Canine" # CLASS ATTRIBUTE 
    # Feline

    # FUNCTIONS/METHODS                                                 FOOD CALCULATION:
    def __init__(self, name, sound, age):                              # 200g to 500g -> 50g of food
        self.name=name  # ATTRIBUTE                                    # 501g to 1kg -> 100g of food
        self.sound=sound                                               # 1.1kg to 2kg -> 150g of food
        self.age=age                                                   # 2kg to 3kg -> 200g of food
                                                                       # 3kg and above -> 3 days water fasting
    
    def ageCalculator(self,dob,dop,status):
        age=dop-dob
        if status ==  "Alive":
            return age
        else:
            return "Sorry for your loss"
        

firstDog = Dog(name="Chu Chu",sound="Kui kui", age='3 days')
secondDog = Dog("Dohode","Dhau Dhau", "3 months")
# dohoDe = Dog()
pinky = Dog("Pinky","Lati","17 days")
print(firstDog.species) #Canine
print(firstDog.sound)   
print(firstDog.age)
print(pinky.sound)
print(pinky.species)
print(firstDog.ageCalculator(20800512,20810909,"Dead"))
# print(dohoDe.species)
# print(pinky.species)





















