# WAP to take user "first name", "mobile number", "address" and add it to list
userDetails=[]
name=input('Enter you first name: ')
userDetails.append(name)
# mobileNumber=input('Enter your mobile no.: ')
userDetails.append(input('Enter your mobile no.: '))
add=input('Enter your address: ')
userDetails.append(add)

# userDetails=[name,mobileNumber,add]
print(userDetails)