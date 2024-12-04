name=input("Enter your name: ")
print(f"Welcome {name}...")
marksObtained_str=input('Enter your marks obtained: ')
fullMarks_str=input('Enter the full marks of the test: ')
marksObtained=float(marksObtained_str)
fullMarks=float(fullMarks_str)

percentage=(marksObtained/fullMarks)*100
print(f"Dear {name} you have secured {percentage}%")
# Grade calculate table
# A+: 90% and above 
# A: 80% and above
# B+: 70% and above 
# B: 60% and above 
# C+: 50% and above 
# C: 40% and above 
# D: 35% and above 
if percentage>=90:
    print(f"Congratulation {name}\nGrade secured: +A")
elif percentage>=80:
    print(f"Congratulation {name}\nGrade secured: A")
elif percentage>=70:
    print(f"Congratulation {name}\nGrade secured: +B")
elif percentage>=60:
    print(f"Congratulation {name}\nGrade secured: B")
elif percentage>=50:
    print(f"Congratulation {name}\nGrade secured: +C")
elif percentage>=40:
    print(f"Congratulation {name}\nGrade secured: C")
elif percentage>=35:
    print(f"Congratulation {name}\nGrade secured: D")
else:
    print(f"Sorry {name}, you have Failed")