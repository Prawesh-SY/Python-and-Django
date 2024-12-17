myList=['ram','hari',9,7]
print(myList,type(myList))
myList[0]='krishan'
print(myList)

myTuple=('ram','hari',9,7)
print(myTuple,type(myTuple))
# myTuple[0]='krishan'

myTuple = ("Krishna",9,7,8)
print(myTuple)
print(myTuple[0])

for item in myTuple:
    print(item)


data=[1,2,2,4,4,5,6,5,7,8]
duplicateDataRemoved=list(set(data))
print(data)
print(duplicateDataRemoved)