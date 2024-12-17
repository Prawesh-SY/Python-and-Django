'''
For loop
Syn: for iterating_var in sequesnce:
        statements(s)
Example:
#1 for letter in 'Python':
     print('Current letter: ', letter)

fruits=[']


*Iterable data 
'''
# for letter in 'Python':
#     print('Current letter: ',letter)

# name='Kathmandu'
# for letter in name:
#     add="@"+letter
#     print(add)

'''
Concept of list
first_data=['apple','ball','cat','dog']
'''

# Class Assignment[My style]
items=['apple','ball','cat','dog','elephant','fish']
for things in items:
    if (things[0] =='a' or things[0] == 'e' or things[0] =='i' or things[0] =='u'):
        print(f'It is an {things}')
    else:
        print(f'It is a {things}')

'''
#Sir's style
first_data=['apple','ball','cat','dog','elephant']
for item in first_data:
    if item[0] in 'aeiou':  #item[0] is subset and 'aeiou' is superset
        output='an'
    else:
        output='a'
    sentence='It is '+output+" "+ item
    print(sentence)
'''
# QUESTIONS:
# Is there anyway to run for loop infinitely?
# What is 'in' in the for loop?
# Ans: The keyword 'in' is an operator. 