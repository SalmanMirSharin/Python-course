'''
    step:
        input/Listen
        process/Decide
        output/talkback
'''

from random import random


greet_words =['hi','hello','hey','yo']
bye_words  = ['bye','by','tata','hasta la vista']
durty_words = ['dog','noughty','fuck']


def Listen():
    return input('Say somthing: ')

def Decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(' ')

    #print(broken_words)

    for word in broken_words:
        if word in greet_words:
            #talkback('Hi man')
            talkback(random(greet_words))
            break
        elif word in bye_words:
            talkback('Tata bye bye!')
            break
        elif word in durty_words:
            talkback('You are a bad man,behave your self!')
            break

def talkback(response):
    print(response)


#while True:

command = Listen()
Decide(command)
