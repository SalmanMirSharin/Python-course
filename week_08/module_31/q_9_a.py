# file = open ('words.dat' , 'w') 
# word = '' 
# while word != 'END' : 
#     word = raw_input( 'Enter a word (enter END to quit): ') 
#     file.write ( word + '\n' ) 
# file.close ( )

import os
import glob

# source_path = f'{os. getcwd()}/'

# source_object = glob.glob(source_path)
# print(source_object)

# print('File name :    ', os.path.basename(__file__))
# print('Absolute path of file:     ',
#       os.path.abspath(__file__))

# print(os.listdir())


# file_name =''
# for i in os.listdir():
#     if i.endswith('.txt'):
#         # It will be work if just one txt file stay in current directory.
#         file_name = i 
# print('word stored file name is:',file_name)
# ls =[]
# with open(file_name,'r') as file:
#     fl = file.readlines()
#     ls.append(fl)

# word_len_in_file = len(ls[0])
# print(word_len_in_file,'Word are stored in this file!')

# for word in ls[0]:
#     print(word)


# Complete:

file = open ( 'words.dat' , 'w' ) 
word = '' 
cnt =0
delet_list=['END']
ls = []
while word != 'END':
    cnt+=1
    word = input('Enter a word (enter END to quit): ')
    ls.append(word)
    for words in ls:
        for i in delet_list:
            words =words.replace(i,'')
    file.write(words +'\n')
    if word=='':
        break
file.close()

print()
print('File Name: words.dat')
print('Stored words:',cnt)

clean_val_ls =[]
with open('words.dat','r') as f:
    f = f.readlines()

    for i in f:
        val = i.strip()
        clean_val_ls.append(val)

len = len(clean_val_ls)
for i,item in enumerate(clean_val_ls):
    if i+1<len:
        print(f'{i+1}.{item}')
    elif len==i+1:
        print(f'{len}.END')

