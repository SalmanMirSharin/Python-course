# data=[{'a':5,'b':10},{'x':15,'y':20}]
# for val in data:
#     for key,val2 in val:
#         print(f"Key:{key} Value:{data[key]}")

# for i,v in enumerate(data):
#     for key in data[i]:
#        print(f"Key:{key} Value:{data[i][key]}")


data=[{'a':5,'b':10},{'x':15,'y':20}]
for val,v in enumerate(data):
    for key in data[val]:
        print(f"Key:{key} Value:{data[val][key]}")


