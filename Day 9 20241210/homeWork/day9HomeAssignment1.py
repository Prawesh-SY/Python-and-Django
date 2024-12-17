# WAP to take the details of five friends
command='y'
totalData=[]
while command=='y':
    userDetails=[]
    name=input('Enter you first name: ')
    userDetails.append(name)
    # mobileNumber=input('Enter your mobile no.: ')
    userDetails.append(input('Enter your mobile no.: '))
    add=input('Enter your address: ')
    userDetails.append(add)
    totalData.append(userDetails)
    command=input('Do you wish to continue (y/n): ')
print(totalData)
print(userDetails)