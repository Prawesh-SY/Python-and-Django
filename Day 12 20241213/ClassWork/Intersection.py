#Intersection Operation in Sets

set1=set()
set2=set()
print("Initializing empty set1: ")
print("Initializing empty set2: ")
for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)
print("Assigning the value to set1: ",set1)
print("Assigning the value to set2: ",set2)
# Intersection using intersection() function
set3=set1.intersection(set2)
print("Intersection of set1 and set2 using 'intersection()' constructor: ",set3)

# Intersection using "&" operator

set4 = set1 & set2
print("Intersection of set1 and set2 using '&' orperator: ",set4)
