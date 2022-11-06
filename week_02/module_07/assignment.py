#Problem-1

# l = ["This", "is", "very", "fantastic"]

# def create_string(st):
#     str=''
#     for ch in st:
#         str+=ch+' '
#     print(str)

# create_string(l)



#Problem-2:

# d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

# def create_list(d):
#     ls =[]
#     for k, v in d.items():
#         ls.append([k,v])

#     flat_list =[item for sublist in ls for item in sublist]
#     print(flat_list)

# create_list(d)


# for sublist in ls:
#     for item in sublist:
#         flat_list.append(item)

# print(flat_list)


#Problem-6:

# def clean_string(ch):
#     output=''
#     for ch in s:
#         if (ch.isupper()):
#             output+=ch
#         elif(ch.islower()):
#             output+=ch
#     return output

# s = "P135636::::::,,,,,h;;;;i,,,t--r;,:o..N"   
# output = clean_string(s)
# print(output)


#Problem-7:

# def replace_comma_with_space(string):
#     st=''
#     for i in string:
#         if i==',':
#             st+=' '
#         else:
#             st+=i
#     return st

# s = "I,have,been,practising,python,since,the,course,started"       
# output = replace_comma_with_space(s)
# print(output)


#Problem-9:

# ls = ['car','airplane','bus','rocket']

# st = 'I have a car I have a bus'

# val = st.split(' ')
# #print(val)

# for find,item in enumerate(ls):
#     for sind,vals in enumerate(val):
#         if item == vals:
#            st= st.replace(item,ls[find+1])
#             # print(item,end='')

# print(st)

#Problem-9:: Solve:

# def replace_word(st,replace_with,s):

#     for (find,item) in enumerate(st):
#         for (sind,vals) in enumerate(replace_with):
#             if item==vals:
#                 s= s.replace(item,replace_with[sind+1])
#     print(s)

# replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

# s = '''I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me.'''
# st = s.split(' ')

# replace_word(st,replace_with,s)



#Problem-10:

# a = ['oh', 'Emelia', 'to']

# s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

# def create_new_string(a,s):
#     #For list a:
#     ls_string=''
#     for i in a:
#         ls_string+=i+' '
#     ls = ls_string.lower().split(' ')

#     #For String S:  
#     s = s.replace(',','')
#     st = s.lower().split(' ')

#     #For File Write:
#     for find,item in enumerate(st):
      
#         for sind,vals in enumerate(ls):
#             if item==vals:
#                 if item=='to':
#                     break
#                 else:
#                     item = st[find+1]+' '
#                 with open('out.txt','a') as fileWrite:
#                      fileWrite.write(item.capitalize())

# create_new_string(a,s)
# with open('out.txt','a') as fileWrite:
#     fileWrite.write('Bangladesh ')
      
           

#Problem-2:

# from pyautogui import sleep
# import requests
# import json

# api_url ="https://api.openweathermap.org/data/2.5/weather?q=jessore&appid=4b5f5c378962441c1c0063e2bb400c5c"
# def weather_data(api_url): 
#     response = requests.get(api_url)

#     content = response.content.decode('UTF-8')

#     #convert string to json:
#     dict_content = json.loads(content)

#     tem = dict_content['main']['temp']

#     C = tem-273.15
#     celsius = '{:.2f}'.format(C)

#     while True:
#         sleep(5)
#         print(f'{celsius} celsius')

# weather_data(api_url)


#Problem-3:

# greet_words =['hi','hey','yo','hello']
# bye_words = ['bye','tata','hasta la vista']

# def listen():
#     return input('Say Something: ')

# def decide(commond):
#     broken_words = commond.lower().split(' ')
    
#     for word in broken_words:
#         if word in greet_words:
#             talkback('Say Hi')
#         elif word in bye_words:
#             talkback('Say bye')

# def talkback(response):
#     print(response)

# commond = listen()
# decide(commond)


#Solve-3:

# import pyjokes

# def listen():
#     return input("You can choose:('neutral' or 'chuck' or 'all'): ")
  
# def decide(command):
#     broken_words = command.lower().split(' ')
#     for word in broken_words:
#         if word =='neutral':
#             neutral = pyjokes.get_joke(category='neutral')
#             print(' ')
#             talkback(neutral)
#             print(' ')
#         elif word =='chuck':
#             chuck= pyjokes.get_joke(category='chuck')
#             print(' ')
#             talkback(chuck)
#             print(' ')
#         elif word =='all':
#             all = pyjokes.get_joke(category='all')
#             print(' ')
#             talkback(all)
#             print(' ')

# def talkback(response):
#         print(response)

# def tell_some_jokes():
#     command = listen()
#     decide(command)

# inpu =input('Do you want to continue:(Y/N): ')
# while inpu.lower()=='y':
#     tell_some_jokes()
#     inpu =input('Do you want to continue:(Y/N): ')
#     if inpu.lower=='n':
#         break


#Problem-4:

# def print_hi():
    
#     return 'hi'

# print(print_hi()) # you can't change this lin  


#It's a out side code:
# def alpha_bet():
#     alpha=''
#     for i in range(0,256):
#         if chr(i)>='A' and chr(i)<='Z':
#             alpha+=chr(i)+' '
#     return alpha

# alpha = alpha_bet()
# print(alpha)
    

#Problem-8:
# #Main function:
# def make_upper(st):
#     return st.upper()

# def make_capital(st):
#     return st.capitalize()

# def make_lower(st):
#     return st.lower()


# #For UpperCase:
# stu = 'i love python'
# upper = make_upper(stu)
# print(upper)

# #For Capitalize:
# stc = 'i love python'
# capitalize = make_capital(stc)
# print(capitalize)

# #For LowerCase:
# stl ='I LOVE PYTHON'
# lower = make_lower(stl)
# print(lower)


# # For test:
# def test_script():
#     is_str_upper ='I LOVE PYTHON'
#     assert is_str_upper == make_upper(stu),'test fail'
#     is_str_capital ='I love python'
#     assert is_str_capital == make_capital(stc),'test fail'
#     is_str_lower = 'i love python'
#     assert is_str_lower == make_lower(stl),'test fail'
# test_script()









# def num(n):
#     if n==50:
#         return True
#     else:
#         return False

# n = int(input())
# val = num(n)
# print(val)

# def test():
#     is_true = True
#     assert is_true == num(n),'test fail'

# test()
	
