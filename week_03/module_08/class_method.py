# class Phone:
#     color ='black'
#     feature = ['camera','water proop','can be use as hammar']

#     def call(self):
#         print('ring ring ring')
    
#     def send_sms(self,number,text):
#         sms = f'The sms is: {text} and the number is: {number}'
#         return sms


    

# my_phone = Phone()
# my_phone.call()

# sms = my_phone.send_sms('01715575340','I missed to miss you my love :)')
# print(sms)


class calculator:
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b
    
    def multipul(self,a,b):
        return a*b
    
    def division(self,a,b):
        return a/b

cal = calculator()

add = cal.add(2,3)
sub = cal.subtract(2,3)
mul = cal.multipul(2,3)
div = cal.division(2,3)

print(add)
print(sub)
print(mul)
print(div)

