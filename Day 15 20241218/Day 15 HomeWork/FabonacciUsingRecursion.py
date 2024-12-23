def fabonacci(n,a=0,b=1):
    print(b)
    if n == 1:
        return "Thank you"
    
    else:
        return  fabonacci(n-1,b,a+b)
    
result = fabonacci(7)
print(result)