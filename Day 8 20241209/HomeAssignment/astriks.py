# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")

'''
# WAP to print:
*****
****
***
**
*
'''
for i in range(5,0,-1):
    for j in range(i):
        print('*', end=" ")
    print('\n')
