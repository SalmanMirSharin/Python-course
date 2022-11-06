

def reverse(s):
    st = s.split(' ')
    str=''
    for item in st:
        item = item[::-1]
        str+=item+' '
    print(str) 
s = "Programming Hero is the best"
reverse(s)
