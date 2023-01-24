# Simple function:
# def greet():
#     print("Good Morning!")
# greet()

# lambda function:
# a = lambda : print('Good Morning.')
# a()

# Example - 1
# s ='Phitron'
# new_string = lambda string_ : string_.upper()[::-1]

# print(new_string(s))

# Example - 2
# mx = lambda a,b : a if(a>b) else b
# print(mx( mx(30,100), mx(10,50) ))

# Example - 3
# ls = [1,2,3,4,5,6,7]

# new_list = [lambda a=i : a*2 for i in ls]
# for l in new_list:
#     print(l())


# Example - 4
# filter,map,reduce

# my_list=[1,2,3,4,5,6,7,8]
# new_list = list(filter(lambda i :(i%2==0),my_list))
# print(new_list)

# Example - 5
# string_list =['Hello','world','python']

# new_string = list(map(lambda x : x.upper(),string_list))
# print(new_string)

# Example - 6
from functools import reduce

lst = [1,2,3,4,5,6,7,8,9,10]

sum = reduce(lambda x,y : x+y,lst)
print(sum)
