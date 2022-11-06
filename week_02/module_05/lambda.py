
from unittest import result


squir = lambda x:x*x

result = squir(3)
#print(result)

# number = [12,35,56,89,23]

#duble_it = lambda x: x*2

# doubled_number = map(duble_it,number)

# print(list(doubled_number))

#num =(10,20,30)

#name ={'rakib':24,'abir':35,'sabbir':32}

# def fun(x):
#     return x*2

#fun = lambda x: x*2

# double_it = map(lambda x:x*2,name)
# print(list(double_it))

# nums = [15,98,30,55,50,65]

# bigger_num = filter(lambda num: num>20 ,nums)

# print(list(bigger_num))

actors = [{'name': 'Sakib','age':64},{'name':'akib','age':50},{'python': 'learner','age':35}]
junior_actors = [{'name': 'Sakib','age':24},{'name':'akib','age':50},{'python': 'learner','age':35}]

valu = filter(lambda actor:actor['age']<35,junior_actors)

print(list(valu))