command="y"
while (command=="y"):
    num_str=input("Input a number: ")
    num=int(num_str)
    if num%2==0:
        print("The number is even")
    else:
        print('The number is odd')
    command = input('Do you wish to contine (y/n): ')