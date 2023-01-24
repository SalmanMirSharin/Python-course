
num = int(input())
x = 0
for i in range(num):
    ls = []
    for j in range(1,num+1):
        ls.append(j)

    ls.pop(0)

    ls.insert(x,1)
    x+=1
    for k in ls:
        print(k,end='')
    print()




