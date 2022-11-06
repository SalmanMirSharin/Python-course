'''All About mankind'''


class Human:
    def __init__(self,gender,height,weight,):
        self.gender = gender
        self.height =height
        self.weight = weight

class Police(Human):
    def __init__(self, gender,height, weight,cases,nationality):
       
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality

class CsEngineer(Human):
    def __init__(self, gender, height, weight,love_to_code,has_gf):
        super().__init__(gender, height, weight)
        self.love_to_code = love_to_code
        self.has_gf = has_gf

if __name__=='__main__':
    police = Police('Femail','5.5ft',60,True,'Bangladeshi')
    print(police.height)

    eng = CsEngineer('Male','65 inch',60,True,False)
    print(eng.has_gf)

    print('Eng 2')
    eng2 = CsEngineer(height='67',weight=50,gender='Male',love_to_code=True,has_gf=False)
    print(eng2.height)




# def func(a:bool,b:bool) ->bool:
#     return a==b

# sum = func(True,True)
# print(sum)