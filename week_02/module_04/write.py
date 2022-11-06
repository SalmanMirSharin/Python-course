# with open('message.txt','a') as fileWrite:
#     fileWrite.write(" Because it is impresive!")

with open("message.txt",'r') as flread:
   text =  flread.read()
   print(text)