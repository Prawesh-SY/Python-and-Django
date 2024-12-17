num="012345678987656"
max=int(num[0])
min=int(num[0])
# print(type(max))
try:
    userInput=int(input("Please choose an option:\n1. Find the heighest number\n2. Find the lowest number"))

    if userInput=='1':
        for i in num:
            
            if int(i)>max:
                max=int(i)
                # print(type(max))
                print(max)
    # print(type(i)) 
    elif userInput == "2":
        for i in num:
            
            if int(i)<min:
                max=int(i)
                # print(type(max))
            
        print(min)
    else:
        print("Invalid Input")
except:
    print("Please enter Interger")
print("Thank you!!!")
67
