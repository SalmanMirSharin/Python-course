from msilib.schema import Error


def func(arg1, arg2, arg3=4, arg4=5):
    print(arg1, arg2, arg3, arg4)

func(1,arg2=20)

# a) fun(6,7) = Answer: 6 7 4 5;
# b) func(4, 5, arg3=6) = Answer: 4 5 6 5;
# c) func() = Answeer: We will get TypeError for missing Argument;
# d) func(3, 4, arg2=1) = Answer: We will get TypeError for arg2 variable;
