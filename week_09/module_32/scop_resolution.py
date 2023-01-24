from math import pi
print(pi)
pi = 34.33

def outer_scop():
    pi = 33.64

    def inner_scop():
        pi = 3.12
        print(pi)
    inner_scop()
    print(pi)
outer_scop()
print(pi)
