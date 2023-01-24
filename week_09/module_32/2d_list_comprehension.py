# Example - 1
# ls =[[j for j in range(3)] for i in range(4)]
# print(ls)


# For practice:

# l = [0]*5
# print(l)

# r,c = (5,3)
# ls = [[0]*c]*r
# ls[0][0] = 1
# print(id(ls[0]))
# print(id(ls[1]))

# ls =[[0 for j in range(5)] for i in range(5)]
# # print(id(ls[0]))
# # print(id(ls[1]))
# ls[0][1] = 1
# print(ls)

# lst =[[1,2,3],[4,5],[6,7,8]]
# print(lst)
# new_list =[sublist for val in lst for sublist in val]
# print(new_list)

# lst = [['Hello','World'],['Mango','Banana'],['Python','Java']]

# new_lst = [sublist for val in lst for sublist in val if len(sublist)>5]
# print(new_lst)

# new_lst = [len(sublist) for val in lst for sublist in val]
# print(new_lst)