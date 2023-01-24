# Global scope
# s = 'I am in Global scope'

# Local scope
# def fun():
#     s = 'I am in Local Scope'


# def outer():
#     s ='outer scope'
#     # Enclosed Scope
#     def inner():
#         s = 'I am in enclosed Scope'

#     inner()
# outer()


from math import pi
print(pi) # Builtin Scope

pi = 34.55 # Global Scope

def outer_scope():
    pi = 32.44 # Local Scope
    def inner_scope():
       pi = 3.36 # Enclosed Scope
       print(pi)
    inner_scope()
outer_scope()
    




