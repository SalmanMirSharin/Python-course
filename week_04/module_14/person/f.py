


class Phone:

    property_list = []

    # def get_phone(self):
    #     return self.property_list

    def list_of_feather(self,feather):
        
        self.property_list.append(str(feather).split(','))


class feather(): 
    def __init__(self,color,price,weight) :
        self.color = color
        self.price = price
        self.weight = weight
    def __repr__(self) -> str:
        return f'{self.color},{self.price},{self.weight}'

f = feather('Black',29999,333)
phn = Phone()

phn.list_of_feather(f)

print(phn.property_list)



# print(feather.property_list)