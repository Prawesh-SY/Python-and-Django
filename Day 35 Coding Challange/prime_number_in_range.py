def is_prime(num):
    count = 0
    for divider in range(2,int(num**(1/2)+1)):
        # print(f"{num} % {divider} = ",num%divider)
        if  num % divider == 0:
            count += 1
            # print(count)
    if count >= 1:
        return False
    else:
        return True
                       

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
primeNumbers = []

for i in range(start,end+1):
    # print(i)
    condition = is_prime(num=i)
    if condition:
        primeNumbers.append(i)

print(primeNumbers)