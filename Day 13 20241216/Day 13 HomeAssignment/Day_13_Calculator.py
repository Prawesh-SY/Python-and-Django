def sum(operand1,operand2):
    result=operand1+operand2
    return result
def sub(operand1,operand2):
    result=operand1-operand2
    return result
def product(operand1,operand2):
    result=operand1*operand2
    return result
def quotient(operand1,operand2):
    result=operand1/operand2
    return result
def exponent(operand1,operand2):
    result=operand1**operand2
    return result
operand1=float(input("Enter a number: "))
operator=input("Enter operator('+' or '-' or '*' or '/' or '**'):")
operand2=float(input("Enter another number: "))
if operator=='+':
    result=sum(operand1,operand2)
    print(f"{operand1} {operator} {operand2} = ",result)
elif operator=="-":
    result=sub(operand1,operand2)
    print(f"{operand1} {operator} {operand2} = ",result)
elif operator=="*":
    result=product(operand1,operand2)
    print(f"{operand1} {operator} {operand2} = ",result)
elif operator=="/":
    result=quotient(operand1,operand2)
    print(f"{operand1} {operator} {operand2} = ",result)
elif operator=="**":
    result=exponent(operand1,operand2)
    print(f"{operand1} {operator} {operand2} = ",result)