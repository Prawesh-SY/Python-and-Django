
# My attempt
"""
command='y'
student=[{'name':'','id':'','eng':'','nep':'','math':'','sci':'','sst':'','optmath':'','acc':''}]
index=0
while command=='y':
    student[index['name']]=input("Enter the student's name: ")
    command=input('Do you wish to add the info of next student (y/n): ')

print(student)
"""
# Guided attmept
command='y'
students=[]
while command=='y':
    student={
        'name':'',
        'id':'',
        'English marks':'',
        'Nepali marks':'',
        'Mathematics marks':'',
        'Science marks':'',
        'Optional I marks':'',
        'Optional II marks':''
    }
    # student['name']=input("Enter student's name: ")
    # print(f"Welcome {student['name']}")
    for key in student:
        student[key]=input(f"Enter {key} of the student: ")
    students.append(student)
    command=input('Do you wish to add next student (y/n): ')
print(students)