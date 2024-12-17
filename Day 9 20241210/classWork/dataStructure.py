#List

firstList=['Apple','ball','sam',99,'9.0',4.3]
print("The elements in the firstList: ",firstList[1:len(firstList):1]) #syntax: print(<listName>[start:stop:step])
print("The elements in the firstList displayed in the reverse ordre:",firstList[::-1])  #:: ->default value

firstList.append("cat")

print("\n")


secondList=list((5,9,'cat','dog'))
print("The elements in the secondList: ",secondList)