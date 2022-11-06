#Problem 1:
# a = input("Enter a word: ")

# for ch in a:
#     if(ch==ch.upper()):
#         print(ch.lower(),end="")
#     elif(ch==ch.lower()):
#         print(ch.upper(),end="")

############-------------------############

# a = chr(97-32)

# print(a)







# def low():
#     l=''
#     for le in range(97,123):
#          l +=(chr(le))
#          return l

# def up():
#     for le in range(65,91):
#         return (chr(le))


# print(low())


# a = 'ThiS'

# for ch in a:
#     if(ch==up()):
#         print(low(),end="")
#     elif(ch==low()):
#         print(up(),end="")



#problem-2:

# num = int(input("Enter the Number: "))

# for n in range(num):
#     for i in range(n):
#         print(i+1,end=' ')
#     print('')
        

#Problem-3:


# def febonacci(n):
#     if(n<0):
#         print("Increate input")
#     if(n==0):
#         return 0
#     elif(n==1 or n==2):
#         return 1
#     else:
#        return febonacci(n-1) + febonacci(n-2)

# num =10
# for i in range(num):
#     print(febonacci(i))


#Problem-4:

from itertools import count
from unicodedata import digit


st ="AbD1@3c"
cnt =0
# upperCase = 0
# LowerCase = 0
# digi = 0
# specialChar = 0
for i in st:
    if(i.isdigit()==True):
        #digi+=1
        cnt+=1
        print("Digit: ",cnt)
    elif(i.upper()==i):
        #upperCase+=1
        cnt+=1
        print("UpperCase: ",cnt)
    elif(i.lower()==i):
        #LowerCase+=1
        cnt+=1
        print("LowerCase: ",cnt)
    else:
        #specialChar+=1
        cnt+=1
        print("Special Char: ",cnt)


#print(count)
# print("UpperCase",upperCase)
# print("LowerCase",LowerCase)
# print("Digit",digi)
# print("SpecialChar",specialChar)


# a = 'abc125'

# for le in a:
#     if(le.isdigit()==True):
#         print(le)