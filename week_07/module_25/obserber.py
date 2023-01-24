class GroupChat:
    def __init__(self):
        self.__observer = []
    
    def attach(self,observer):
        self.__observer.append(observer)

    def add_new_message(self,msg):
        self.notify(msg)

    def notify(self,nsg):
        for observer in self.__observer:
            observer.uptodate(nsg)
    
class Observer:
    def __init__(self,name) -> None:
        self.name = name

    def uptodate(self,msg):
        print(f'New Message for: {self.name}: {msg}')


messenger = GroupChat()
abid = Observer('Abid')
nabid = Observer('Nabid')
sabid = Observer('Sabid')

messenger.attach(abid)
messenger.attach(nabid)
messenger.attach(sabid)

messenger.add_new_message('Hey bro and sis!')