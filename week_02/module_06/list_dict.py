my_list =['@1F','OBCD','!g','@F2','ABCG','!e','@F3','GDEG','!yy']

output_dict ={}

for index,val in enumerate(my_list):
    if val[0]=='@':
        output_dict[val] = my_list[index+1]
 

print(output_dict)