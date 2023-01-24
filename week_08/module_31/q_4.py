
v =['Saturday','SunDay','Monday','Tuesday','Wednesday','Thursday','Friday']
ls =[]
for i in range(7):
    try:
        week =int(input(f'{v[i]}: '))
        ls.append(week)
    except:
        print('Please Enter integer value!')
        exit()

print('Minimum rainfall: ',min(ls))
print('Maximum rainfall: ',max(ls))


