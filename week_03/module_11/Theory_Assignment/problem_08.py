
#It is write by simple way:
# s = [10,20,10,40,50,60,70]
# le = len(s)
# target =50
# for i,val in enumerate(s):
#     if i<le-1:
#         if target==(s[i]+s[i+1]):
#             print(i+1,i+2)
#         # sum= (s[i]+s[i+1])
#         # #print(s[i]+s[i+1])
#         # ls.append(sum)
# # print(ls)


#It is write by Opp:
# class Sums:
#     def __init__(self,*arg) :
#         self.ls = [*arg]
#         self.len = len(arg)

#     def put(self,target):
#         for i,val in enumerate(self.ls):
#             if i<self.len-1:
#                 if target==(self.ls[i]+self.ls[i+1]):
#                     print(i+1,i+2)                          
    
# sm = Sums(10,20,10,40,50,60,70)

# sm.put(50)