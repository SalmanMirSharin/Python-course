
#write by simple approch:

# def get_subset(arr):
#     subset =[[]]
#     for elem in arr:
#         for i in range(len(subset)):
#             subset.append([subset[i]+elem])
#             #print(i)
    
#     return subset
# ls =[1,2,3]
# set = get_subset(ls)
# print(set)


#Write by use class approch:
class Subset:
    def __init__(self,*arr):
        self.ls = [*arr]
        self.subsets =[[]]
        
    def set(self):
        for elem in self.ls:
            for i in range(len(self.subsets)):
                self.subsets.append(self.subsets[i]+[elem])
        print(self.subsets)

subset = Subset(4,5,6)
subset.set()