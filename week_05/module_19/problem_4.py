# anagrams = (['eat', 'ate', 'done', 'tea', 'soup', 'node'])

# s =[]

# st1 ='this'
# st2 ='sith'

# if len(st1)!=len(st2):
#         pass



# for i,val in enumerate(st1):
#     if st1[i] != st2[i]:
#         pass
#     else:




# st1 ='this'
# st2 ='sith'

# ls =['this','sith']

# st1 = ''.join(sorted(st1, key=str.lower))
# st2 = ''.join(sorted(st2, key=str.lower))

# print(st1)
# print(st2)

anagrams = (['eat', 'ate', 'done', 'tea', 'soup', 'node'])

st ={}
for i in anagrams:
    val = ''.join(sorted(i, key=str.lower))

    if val in st:
        st[val].append(i)
    else:
        st[val] = [i]

anagrams =[]
for key,valus in st.items():
    anagrams.append(valus)

print(anagrams)






# anagrams = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']

# grouped_anagrams = {}

# for string in anagrams:
#     # print(string)

#     sorted_string = str(sorted(string))
#     # print(sorted_string)

#     if sorted_string in grouped_anagrams:
#       grouped_anagrams[sorted_string].append(string)
#     #   print(grouped_anagrams)
#     else:
#          grouped_anagrams[sorted_string] = [string]
#         #  print(grouped_anagrams)

# print(list(grouped_anagrams.values()))