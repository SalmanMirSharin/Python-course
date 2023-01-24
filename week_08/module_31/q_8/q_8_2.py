# With recursion:

# def max(l,n):
#     if l==[]:
#         return n
#     elif l[0]>n:
#         return max(l[1:],l[0])
#     else:
#         return max(l[1:],n)

# l = [1000,50,15,100,10]
# n= 500
# mx = max(l,n)
# print(mx)


# Without recursion:

def max(l,n):
    for i in l:
        if i>n:
            n = i
    return n
l = [20,50,15,100,10]
n = 50
mx =max(l,n)
print(mx)
