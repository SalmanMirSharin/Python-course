# ls =[1,2,3]
# ls2 =['one','two','three']

# print(list(zip(ls,ls2)))


names = ['rahim','karim','halim']
salaries = [10000,20000,15000]
result = list(zip(names,salaries))

# new_dict = {name:salary for name,salary in zip(names,salaries)}
# print(new_dict['karim'])

name,salary = zip(*result)
print(name)
print(salary)