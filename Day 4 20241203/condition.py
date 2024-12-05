command ='y'
while (command=="y"):
    name=input("Enter your name: ")
    age_str = input("Enter your age: ")
    age=int(age_str)
    # while age_str.isalpha():
    #     age_str=input("Age invalid...\nEnter your age: ")


    # if age>18:
    #     print("You can drink")  

    # age = 13
    # if age<18:
    #     print("You like chocolate") 

    # if age>20:
    #     print("You are eligible to marry")
    #     print("You are eligible to have Driving License")
    #     print("You are eligible to drink")
    #     print("You are eligible to work")
    # else:
    #     print("You like chocolate")
    #     print("You are suppose to be in school")
    #     print("You are suppose to be study")


    # Hint: if isinstance(age,str) and age.isdigit()==False
    # failed attemp:if age_int.isdigit() == False:    # Sir's method: if not age.isdigit(); My method:if age != age.isdigit():[Incorrect]
    print(f'Welcome {name},\n')
    if isinstance(age_str,str) and age_str.isdigit()==False:
        print('Please intput digit in the age field')    
    elif age<0 or age>150:
        print('Invalid age')
    elif age<13:
        print('You are a child')
    elif age>=13 and age<20:
        print('You are a teenager')
    elif age>=20 and age<=60:
        print('You are an adult')
    elif age>60 and age<=65:
        print('You are senior citizen')
    else:
        print('You are senior citizen and entitled to receive Senior Citizen Pension')
    command=input('Do you wish to check again (y/n): ')
        # How to execute multiple statements in the true condition of if?
        # Ans: Indentations should be at same level
        # New line is ignored
        # Indentation is considered
