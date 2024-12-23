class calculator:
    outputSentence="The output of the expression: "     # 'outputSentence' is called CLASS ATTRIBUTES
    def sum(self, a, b):
        print(self.outputSentence + f"{a} + {b} = ",a+b)  # 'a' and 'b' are called FUNCTION ATTRIBUTES
    def sub(self, a, b):
        print(self.outputSentence + f"{a} - {b} = ",a-b)
    def product(self, a, b):
        print(self.outputSentence + f"{a} * {b} = ",a*b)
    def quotient(self, a, b):
        print(self.outputSentence + f"{a} / {b} = ",a/b)
    def exponent(self, a,b):
        print(self.outputSentence + f"{a} ^ {b} = ",a**b)

c1=calculator()
c1.sum(3,2)
c1.sub(3,2)
c1.product(3,2)
c1.quotient(3,2)
c1.exponent(3,2)

"""
Notes
if we dont use 'self' then we will have to call the function by  using 'calculator.sum(3,2)' """