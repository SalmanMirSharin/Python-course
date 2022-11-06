
class A:
    val = [10]
    def __init__(self,val) -> None:
        self.val.append(val)
    
a=A(100)
b=A(200)
print(a.val)