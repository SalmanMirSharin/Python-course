# d ={{}}
# d['continent']['country']= 'Bangladesh'
# print(d)


# d = {}
# ini = input("djidd")
# d[ini] ={}
# d['conti'] ={}
# d['continent']['country']= 'Bangladesh'
# d['conti']['country'] = 'India'

# print(d)



# d ={}

# d = {"key" : {}, "key2" : {}, "key3" : {}}



# dct = {}
# for k in range(0,4):
#     dct[k] = {}
#     user_input = input("")
#     dct[k][k+1] = user_input
# print(dct)


















# def val():
#     st = ''
#     for i in range(10):
#         v =i*2
#         st+=str(v)
#     return st

# all_val = int(val())
# print(all_val)


# def val():
#     val = []
#     for i in range(10):
#         v =i*2
#         val.append(v)
#     return val

# print(val())


# for i in range(5):
#     def add(x):
#         return x*2
#     print(add(i))


# for i in range(5):
#     def add(x):
#         return x*2
#     print(add(i))


# for i,val in enumerate(range(5)):
#     if i==1:
#         continue
#     else:
#         print(val)

data = [val+1 for i,val in enumerate(range(5)) ]
print(data)
dct ={i+1:data for i in range(5)}
print(dct)