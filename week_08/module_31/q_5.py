
v =['Saturday','SunDay','Monday','Tuesday','Wednesday','Thursday','Friday']
ls =[]
for i in range(7):
    try:
        week =int(input(f'{v[i]}: '))
        ls.append(week)
    except:
        print('Please Enter integer value!')
        exit()

sum = 0
for sm in ls:
    sum+=sm

mean = sum/7
print('mean value: ',mean)

s = []
for div in ls:
    val = div-mean
    s.append(val**2)

sm =0
for i in s:
    sm+=i
deviation = (sm/6)**0.5
print('Deviation value: ',deviation)













