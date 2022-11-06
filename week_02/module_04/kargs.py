# def add(num1,*number):
#     print(num1)
#     print(number)

# add(2,3,5,7,9)

# def full_name(**name):
#     print(name)

# full_name(first="Dr.",second="Rahaman",last="Ali")

# def long_name(first,last, **name_part):
#     print(first,last,name_part)

# long_name("Abdul","Hamid",middle = "Khan")


def all_name(first,*args,**kargs):
    # print(first)
    # print(args)
    # print(kargs)
    for key,value in kargs.items():
        print(f'{key}: {value}')

all_name('adb','ddd','ccc','bbb',name='abul',father='babul')