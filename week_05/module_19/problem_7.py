# import keyboard
# import time

# if keyboard.read_key()=='a':
#     print('Hey, I am a!')

# if keyboard.read_key()=='enter':
#     print('I am Enter key!')


# if keyboard.read_key()=='enter':
#             print(a[0])




# with open('File.txt','r') as f:
#     page = f.read()

# page = page.split('--')

# while True:
  
#     for i in page:
#         print(i)
      
        # print("1.Press 'Enter' to read more:")
        # print("1.Press 'q' to quit:")
#         # print()
        
#         if keyboard.read_key()=='q':
#             print('print how..')
#             break
#         # print(i)
#         # print()






    # if keyboard.is_pressed('a'):
    #         break
        # keyboard.wait('enter')
   

 


    
    
# keyboard.press_and_release('q')




# for i, val in enumerate(page):
#     # if i ==0:
#     #     print(page[0])
#     # else:
#     #     # if keyboard.read_key()=='delete':
#     #     if  keyboard.press_and_release('enter'):
#     #         # if i<len(page):
#     print(val)
#     keyboard.wait('enter')



            
#                 # print(page[i]
   
# #  print(len(page)-1)



# k = input()

# if k=='q':
#     print('Hey')



import keyboard
 
with open("File.txt", "r") as f:
    page = f.read()
 
page = page.split("--")

i = 0
print(page[i])
i += 1
 
while True:
    print()
    print("1.Press 'Enter' to read more:")
    print("1.Press 'q' to quit:")
    print()
    k = keyboard.read_key()
    if k == "q":
        break
    elif k == "enter":
        print(page[i])
        i += 1
        k = keyboard.read_key()
    if len(page) == i:
        i = 0

