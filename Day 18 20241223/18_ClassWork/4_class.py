class Calculator:

    def __init__(self, firstNum, operator, secondNum):
        print("Initializing the object....")
        self.operator=operator
        self.firstNum = firstNum
        self.secondNum = secondNum
        pass

    def result(self):
        if self.operator == "+":
            return self.add()
        elif self.operator == "-":
            return self.sub()

    def add(self):
        return self.firstNum + self.secondNum
    def sub(self):
        return self.firstNum - self.secondNum

myList=[1,2]

cal=Calculator(4,"-",8)
op=cal.result()
# ca=Calculator(myList)
# c=Calculator(4)

print("RESULT = ",op )
