


def nearly_equal(a,b):
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i] == b[j]:
            i+=1
            j+=1
        else:
            j+=1
        
    if i==len(a):
        print(True)
    else:
        print(False)

a = 'perl'
b = 'pearl'
nearly_equal(a,b)