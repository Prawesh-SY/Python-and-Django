"""
List compression

"""
data=[1,2,3,4,5,6]
dataCentury=[i+100 for i in data]


#WAP to get a list of even numbers using list compression
dataEvenUsingListCompression= [j for j in data if j%2==0]
 

dataEvenUsingLoop=[]
for k in data:
    if k%2==0:
        dataEvenUsingLoop.append(k)

print("Original data list: ", data)
print("Adding 100 to each item using List Compression Method: ",dataCentury)
print("Extracting even numbers from the original list using List Compression Method: ",dataEvenUsingListCompression)
print("Extracting even numbers from the original list using for loop: ",dataEvenUsingLoop)