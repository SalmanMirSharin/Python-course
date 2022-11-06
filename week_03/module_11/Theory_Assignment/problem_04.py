




# l = list(a)

# for i,val in enumerate(l):
    
#     if i%2==1:
#         for it in range(int(val)):
#             for v in range(it):
#                 if val%2==0:
#                     print(v)


# from cgi import print_arguments


# a = ['x','y','c']
# # l = [2,5,7]
# l = ['x','y','z']

# # i=0
# # while i<len(l):
# #     for j in l[i]:
# #         print(j)
# #     i+=1


# # # for t in range(i):
# # #     print('Hey')

# # for ind, i in enumerate(l):
# #    for a in range(i):
# #         if a<i:
# #             print('x')
# #             break

# for i in l:
#     for j in range(2):
#         print('x')
#             # pass
#             #print(a[1])
        
# # print(a[0])


s = input('Enter value: ')
l1 =[]
l2 =[]
for ch in s:
    if ch.isdigit():
        l2.append(int(ch))
    elif ch.isupper() or ch.islower():
        l1.append(ch)

st=''
for i , val in enumerate(l1):
    for j in range(l2[i]):
        #print(l1[i])
        st+=l1[i]

sort = ''.join(sorted(st,key=str.casefold))
print(sort)
        





# sorting system by str.casefold

# x = ['Aden', 'abel']
# x.sort(key=lambda y: y.lower())
# #  x
# # ['abel', 'Aden']

# print(x)

# x ='VariAble'

# # st = ''.join(sorted(x,key=lambda s: s.lower()))
# st = ''.join(sorted(x,key=str.casefold))
# print(st)