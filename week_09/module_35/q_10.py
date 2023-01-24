# Single inheritance:
class Parent:
    pass

class Child(Parent):
    super().__init__()
    pass


# Multiple inheritance:
# class GrandParent:
#     pass

# class Parent:
#     pass

# class Child(Parent,GrandParent):
#     pass


# Multilevel inheritance:

class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass