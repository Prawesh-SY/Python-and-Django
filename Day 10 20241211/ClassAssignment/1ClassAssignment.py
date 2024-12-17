
userDetail={'name1':'Ram','number1':'+9779865122175','name2':'Sam','number2':'9845119833'}
print(userDetail)
for key in userDetail:
    if "number" in key:
        if '+977' not in userDetail[key]:
            userDetail[key]='+977'+userDetail[key]

print(userDetail)

# Sir's Method

for key in userDetail:
    if key == "number1":
        userDetail["number1"]="+977"+userDetail['number1']
    
print(userDetail)