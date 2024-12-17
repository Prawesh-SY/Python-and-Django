# WAP to print reverse of "tribhuwanuniversity"
string='tribhuwanuniversity'
index=len(string)
print("Sir's Method")
print(string[::-1]) #
# print(index)
print("My method")
reverse_string=''
rev_str=''
for x in string: #
    reverse_string=reverse_string+(string[index-1])
    index=index-1
print(reverse_string)

print("Friend's method")
index = len(string)
for i in range((index-1),-1,-1):
    rev_str=rev_str+string[i]
print(rev_str)

print("Sir's method")
print(string[len(string):0:-1])
    
# print(y)
# WAP to print reverse from 25 to 15
# for x in range(25,14,-1):
#     print(x)