# With recursion:

# def mylen(l,n):
#     if l==[]:
#         return n
#     else:
#         return mylen(l[1:],n+1)

# ls = [1,2,3,4,0,7]
# n = 5
# my =mylen(ls,n)
# print(my)

# Without recursion:

def mylen(l,n):
    ln = len(l)
    return ln+n

ls = [1,2,3,4,0,7]
n = 5
my =mylen(ls,n)
print(my)