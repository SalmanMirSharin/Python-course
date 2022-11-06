# def exicute(f):
#     f('This is a print function!')

# exicute(print)

def dic(func):
    def exe():
        print('Execute First!')

        func()
        print('Execute last!')
    return exe

@dic
def who_is_mehedi():
    print('Mehedi is a good boy!')


# dic = dic(who_is_mehedi)
# dic()

who_is_mehedi()