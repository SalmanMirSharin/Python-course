
a = input('enter numbers: ')

ls = a.split('-')

sum =0
for i in ls:
    sum+=float(i)
print(f'Sum is: {sum}')