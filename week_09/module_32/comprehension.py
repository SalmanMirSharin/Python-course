# list comprehension
# [expresion for item in range()]
# Example - 1
# ls = ['Hello','world','python']

# new_ls = [x.upper() for x in ls]
# print(new_ls)

# Example - 2

# x = [i for i in range(1,11)]
# y = list(range(1,11))
# print(x)
# print(y)

# Example - 4

# lst = [i for i in range(1,20) if i%2==0]
# print(lst)

# Example - 5

# lst = [x for x in range(1,100) if x%3==0 if x%5==0]
# print(lst)

# Example - 6
# lst = ['Even' if x%2==0 else 'Odd' for x in range(100)]
# print(lst)


# Example - 7

# lst = [(x,y) for x in [1,2,5,6,7,11] for y in [3,4,8,9,10,11] if x!=y]
# print(lst)



# Dictionary comprehension

# Example - 1
# dct = {i:i+10 for i in range(10)}
# print(dct)

# Example - 2
# dct = {'jack':30,'rahim':33,'karim':31}

# new_dct = {k:v for k,v in dct.items() if v%2==0}
# print(new_dct)

# Example - 3
# dct = {'jack':30,'rahim':33,'karim':31}

# new_dct = {k:v for k,v in dct.items() if v%2!=0 if v>32}
# print(new_dct)

# Example - 4
# dct = {'jack':60,'rahim':33,'karim':31}
# new_dct = {k:('Old' if v>=50 else 'Young') for k,v in dct.items()}
# print(new_dct)

# Example - 5   ## How can make this dictionary.
# dct = {k1:{k2:k2*k1} for k2 in range(6) for k1 in range(5)}
# print(dct)

# d = {}

# for i in range(5):
#     tmp={}
#     tmp[5]=5*i
#     # print(tmp)
#     d[i]=tmp
# print(d)

d ={}
k2 =5
for k1 in range(5):
    



 

# dct = {}

# dct['a']['b'] = 'c'
# dct['d']['e'] = 'f'

# print(dct)

# ls =[[]]
# ls.append(3)
# ls[0].append(2)
# print(ls)
# ls =[[]]
# for i in range(6):
#     for j in range(5):
#         if j%2==0:
#          ls[0].append(j)
#         else:
#             ls.append(j)

# print(ls)