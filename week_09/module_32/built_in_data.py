# num = 349488439838023239394994303848
# print(num+1)

# ls = [1,2,3,4,5,[3,5,6,[11,34,2,5,[9,5,3,2]]]]
# print(1 in ls)
# ls[5][3][4][1] = 55
# print(ls)

# tp = (1,2,3,4,5,[22,35,56])
# tp[5] = 7
# print(tp)


# dct = {'rahim':15000,'karim':20000}
# print(dct['rahim'])
# print(dct.get('halim'))
# print(dct.get('halim',dct.get('karim')))

# child1 ={
#     'name':'Jack',
#     'year':2002
# }
# child2 ={
#     'name':'emiya',
#     'year':2004
# }
# child3 ={
#     'name':'tom',
#     'year':2000
# }

# family ={
#     'child1': child1,
#     'child2': child2,
#     'child3': child3
# }


# print(family['child1']['name'])
# print(family.get('child2').get('year'))

# a = dict([(1,'A'),(2,'B'),(3,'C'),(4,'D')])
# print(a)
# a.pop(3)
# print(a)
# print(a.keys())
# print(a.values())

# for key,value in a.items():
#     print(f'key {key}: value {value}')


# st = {1,2,2,3,4,5}
# insert() doesn't work to set
# st.insert(0,3)
# print(st)


# st = [1,2,2,3,4,5]
# st.insert(0,3)
# print(st)


# s = '3 I love python'
s = '233454345'
# s[0] ='i'
print(s.upper())
print(s.lower())
print('I' in s)
print(s[0].isalpha())
print(s[0].isnumeric())
print(s.isalnum())
