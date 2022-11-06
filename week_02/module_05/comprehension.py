# number = [12,45,34,67,89,80,20,18,65]

# odd_number = []

# for num in number:
#     if(num%2==1):
#         odd_number.append(num)

#print(odd_number)

# odd_number2 = [num for num in number if num%2==1 if num%5==0]
# print(odd_number2)


name =['sakib','salman','Riaj']

ages =[27,46,18]

# pairs = [(nam, age) for nam in name for age in ages if age<25 ]
# print(pairs)

for nam in name:
    #print(name)
    for age in ages:
        if age<25:
             print(nam,age)
 