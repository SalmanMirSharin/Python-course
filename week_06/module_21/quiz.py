# Q-1
# z=set('abc')
# z.add('san')
# z.update(set(['p', 'q']))
# print(z)


# Q-2
# list1 = [1,2,3,4]
# list2 = [2,4,5,6]
# list3 = [2,6,7,8]
# result = list()
# result.extend(i for i in list1 if i not in (list2+list3) and i not in result)
# result.extend(i for i in list2 if i not in (list1+list3) and i not in result)
# result.extend(i for i in list3 if i not in (list1+list2) and i not in result)
# print(result)

# q-3
# print('*', "abcde".center(6),'*', sep='')

# Q-4

# class change:
#     def __init__(self, x, y, z):
#         self.a = x + y + z
 
# x = change(1,2,3)
# y = getattr(x, 'a')
# setattr(x, 'a', y+1)
# print(x.a)


# Q-5

# class Demo:
#      def __init__(self):
#          self.a = 1
#          self.__b = 1
 
#      def get(self):
#          return self.__b
 
# obj = Demo()
# print(obj.get())


# Q-6

# lst = [1, 2, 3]
# print(lst[3])


# Q-9

# class A:
#      def __init__(self):
#          self.__i = 1
#          self.j = 5
 
#      def display(self):
#          print(self.__i, self.j)
# class B(A):
#      def __init__(self):
#          super().__init__()
#          self.__i = 2
#          self.j = 7  
# c = B()
# c.display()


# Q-10

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()



