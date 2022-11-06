#Simple Approch:
# import math

# def Distence(x1,y1,x2,y2):
#     x = int(math.pow((x1-x2),2))
#     y = int(math.pow((y1-y2),2))
#     sum = x+y
#     sq = math.sqrt(sum)
#     print(sq)
    
# Distence(2,5,1,2)
    

#Writh by Opp Approch:
from math import pow,sqrt
class Distance:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def Compute(self):
        x = int(pow((self.x2-self.x1),2))
        y = int(pow((self.y2-self.y1),2))
        sqt = '{0:.5f}'.format((sqrt(x+y)))
        distance = sqt.split('.')
        le = len(distance)
        for i,val in enumerate(distance) :
            if i<le-1:
                if distance[1]=='00000':
                    print(int(val))
                else:
                   print(f'{val}.{distance[1]}')     

coordinate = Distance(1,2,4,6)
coordinate.Compute()
        




# s ='5.0000'
# st = s.split('.')
# # print(st)

# for i,val in enumerate(st):
#     if st[1]=='00000':
#         print('Hey')
#         break
#     else:
#         print('Nothing')
#         break
        
