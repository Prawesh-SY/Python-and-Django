set_1={5,1,7,5}
print(set_1)
print (type(set_1)) # type: set

set2={}
print(type(set2))   # type: dictionary

#Conversion of list to set  Type casting

list_cast= [1,2,3,1,"sushil","sushil",1.2,1.3,1.2]

listConversionToSet = set(list_cast)
print(listConversionToSet)
print(type(listConversionToSet))
setConversionToList = list(listConversionToSet)
print(setConversionToList)
print(type(setConversionToList))