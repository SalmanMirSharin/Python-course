#Encrypt and deCrypt:


# data = 'firebaby'
# shift =-4
# output_data =''
# for character in data:
#     output_data+=(chr((ord(character)+shift-97)%26+97))
# print(output_data)


data = 'az'
shift =1
output_data =''
for character in data:
    print(chr((ord(character)+shift-97)%26+97))
