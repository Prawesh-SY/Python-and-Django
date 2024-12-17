# WAP to remove duplicate data from the list

# My method failed attempt
firstList = [1,2,3,1,4,] 
secondList=[0]*len(firstList)
for i in range(0,len(firstList)):
    for j in range(0,len(firstList)):  
        if i==j:
            secondList[i]=firstList[j]
        elif firstList[i]!=firstList[j]:
            secondList[j]=firstList[j]

print(firstList)
print(secondList)


# secondList=[]
# for item in firstList:
#     if item in secondList:
#         continue
#     secondList.append(item)

# print(secondList)
# print(firstList)

# for i in firstList:
#     if i not in secondList:
#         secondList.append(i)