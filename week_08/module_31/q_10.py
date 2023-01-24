# class GroupChat:
#     def __init__(self):
#         self.__observer = []
    
#     def attach(self,observer):
#         self.__observer.append(observer)

#     def add_new_message(self,msg):
#         self.notify(msg)

#     def notify(self,nsg):
#         for observer in self.__observer:
#             observer.uptodate(nsg)
    
# class Observer:
#     def __init__(self,name) -> None:
#         self.name = name

#     def uptodate(self,msg):
#         print(f'New Message for: {self.name}: {msg}')


# messenger = GroupChat()
# abid = Observer('Abid')
# nabid = Observer('Nabid')
# sabid = Observer('Sabid')

# messenger.attach(abid)
# messenger.attach(nabid)
# messenger.attach(sabid)

# messenger.add_new_message('Hey bro and sis!')



class Subscriber:
    def __init__(self):
        self.__observer_for_subscriber = []
        self.__observer_for_unsubscriber = []
    
    def subscribe(self,observer):
        self.__observer_for_subscriber.append(observer)

    def unsubscribe(self,observer):
        self.__observer_for_unsubscriber.append(observer)

    def subscribe_channel_name(self,channel):
        self.sub_notify(channel)

    def unsubscribe_channel_name(self,channel):
        self.unsub_notify(channel)

    def sub_notify(self,channel):
        for observer in self.__observer_for_subscriber:
            observer.subs_cribe(channel)

    def unsub_notify(self,channel):
        for observer in self.__observer_for_unsubscriber:
            observer.unsubs_cribe(channel)
    
class User:
    def __init__(self,name) -> None:
        self.name = name

    def subs_cribe(self,channel):
        print(f'{self.name}: you Subscribe the "{channel}" channel!')
    
    def unsubs_cribe(self,channel):
        print(f'{self.name}: you UnSubscribe the "{channel}" channel!')


people = Subscriber()

lee_jong = User('Lee Jong-suk')
lee_min= User('Lee Min-ho')
song_joong= User('Song Joong-ki')

dilraba = User('Dilraba Dilmurat')
zhao_lusi = User('Zhao Lusi')

people.subscribe(lee_jong)
people.subscribe(lee_min)
people.subscribe(song_joong)

people.unsubscribe(dilraba)
people.unsubscribe(zhao_lusi)

people.subscribe_channel_name('Apna college')
print()
people.unsubscribe_channel_name('Code with Harry')


