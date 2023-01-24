data={
    'a':[{
        'aa':{'aax':5,'aay':6,'aaz':7},
        'ab':{'abx':8,'aby':9,'abz':10}
        },
        {
        'aaa':{'aaax':11,'aaay':12,'aaaz':13},
        'aab':{'aabx':14,'aaby':15,'aabz':16}
        }],
    'b':[{
        'ba':{'bax':17,'bay':18,'baz':19},
        'bb':{'bbx':20,'bby':21,'bbz':22}
        },
        {
        'bba':{'bbax':23,'bbay':24,'bbaz':25},
        'bbb':{'bbbx':26,'bbby':27,'bbbz':28}
        }],
    'c':[{
        'ca':{'cax':29,'cay':30,'caz':31},
        'cb':{'cbx':32,'cby':33,'cbz':34}
        },
        {
        'cca':{'ccax':35,'ccay':36,'ccaz':37},
        'ccb':{'ccbx':38,'ccby':39,'ccbz':40}
        }]
}

# print(data)

# for key,val in data.items():
#     print(data[key][1])
    # for j in data[i]:
    #     print(data[i][0])

# print(data['a'][0]['aa']['aax'])

# ls ={'a':[{'aa':1,'aaa':2}],'b':[{'bb':3,'bbb':4}],'c':[{'cc':5,'ccc':6}]}


# for i,val in ls.items():
#     # print(ls[i][0].keys())
#     ls[i][0]+= ls[i][0].keys()

# print(ls['a'][0]['aa'])
# lst = []
# for key,val in ls.items():
#     lst.append(val)
    # print(val)

# print(lst[0][])
# for i,val in enumerate(lst):
#     print(lst[i][0])

# ls= []
# for i in data.keys():
#     # print(data[i])
#     ls.append(data[i])

# for j,val in enumerate(ls):
#     # print(ls[j])
#     for k,l in enumerate(ls[j]):
#         print(l)

# ls 
# for i,val in enumerate(data['a']):
#     # print(data['a'][i].keys())
#     for j in data['a'][i].keys():
#         # print(j)
#         # print(data['a'][i][j])
#         for k in data['a'][i][j].keys():
#             # print(k)
#             print(k,data['a'][i][j][k])   



# print(data['a'])
# ls =[1,2,3,4]

# for i in ls:
#     print(i)


# # Complete Code:
# for key in data.keys():
#     for i,val in enumerate(data[key]):
#         for j in data[key][i].keys():
#             for k in data[key][i][j].keys():
#                 print(f"Key:{k} Value: {data[key][i][j][k]}")  


# for key in data.keys():
#     for i,all_val in enumerate(data[key]):
#         for n in data[key][i].keys():
#             for m in data[key][i][n].keys():
#                 print(f"Key:{m} Value: {data[key][i][n][m]}")  





# We get 4 type of scope in python:
# 1.Global
# 2.Local
# 3.Enclosed(nasted function)
# 4.Builtin


# # Global scope:
# Global scope variable We can access anywhere from code editor. It is independent in code editor
# Like below this variable:


# # Local Scope:
# 	which variable we use inner side of function that variable called Local scope variable. This variable just work inside of function. So local scope is a function finite scope.

# Like below this variable:


for i in range(2):
    for j in range(5):
        if i!=j:
            print(j)