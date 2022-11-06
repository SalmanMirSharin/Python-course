import re


# def do_somthing():
#     print("inside the function, do somthing!")
#     def inner_function():
#          print('Inside the inner function!')
#     inner_function()

# do_somthing()

def first_function():
    print('inside the first function!')
    def second_function():
        print('Inside the second function!')
    return second_function

# first = first_function()
# first()

# first_function()()

