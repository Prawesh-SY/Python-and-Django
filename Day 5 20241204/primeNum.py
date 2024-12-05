command ='y'
while command=='y':
    num_str=input('Enter a number: ')
    num = int(num_str)
    x=0
    count = 1
    while (count <= num):
        mod=num%count
        # print(mod)
        # count = count + 1
        if mod==0:
            # print("Diviser: ",count)  #to print the diviser of the given number
            x=x+1
        if x>=4:    #to reduce the time complexity of the program
            break
        count = count + 1
    if x<3:
        print('The number is prime')
    else:
        print('The number is composite')
    command=input('Do you want to check next number (y/n): ')