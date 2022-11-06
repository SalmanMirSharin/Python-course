
class Find_object:
    count =0
    def __init__(self,name):
        self.name = name
        Find_object.count+=1

    def count_object():
        print(Find_object.count)


my_name = Find_object('Mehedi')
print(my_name.name)
your_name = Find_object("Your Name")
her_name = Find_object("Her Name")
his_name = Find_object("His Name")
my_name = Find_object('Mahadi')
print(my_name.name)
their_name = Find_object("Their Name")

#print(Find_object.count)

Find_object.count_object()