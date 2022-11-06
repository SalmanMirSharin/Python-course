
def exp(a,n):
    num =1
    for i in range(1,n+1):  
        num *= a
    return num
    
a,n = list(map(int,input('Enter numbers: ').split()))

output = exp(a,n)
print(f'result is: {output}')
