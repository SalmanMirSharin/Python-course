
ls = ['this','is','the','things']

strin ='''Bangladesh is a small country. This is my contry. 
I live in country. This country gave me lots of the is'''
strin = strin.lower()
split_words = strin.split(' ')

st=' '
for ch in split_words:
    if ch in ls:
        st+=ch+' '
sp = st.split(' ')

ss = set(sp)

for i in ss:
    print(i)

        
