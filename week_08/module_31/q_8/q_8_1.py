# Recursion:
# def sum_odd(n,total):
#     if n==1:
#         return total
#     elif n%2==0:
#         return sum_odd(n-1,total)
#     else:
#         return sum_odd(n-2,total+n)

# sum = sum_odd(1,2)
# print(sum)

# Without Recursion:

def sum_odd(n,total):
    for i in range(2,n+1):
       if i%2==1:
            total+=i
    return total
sum = sum_odd(5,0)
print(sum)