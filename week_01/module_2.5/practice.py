# Problem:-1
# import math

# floor_ceil = float(input('Enter float value: '))

# floor_value = math.floor(floor_ceil)
# ceil_value =math.ceil(floor_ceil)

# print('floor value:',floor_value)
# print('ceiling value:',ceil_value)


# problem:-2
# num = input('Give value and get positive value:')

# for char in num:
#    if(char=='-'):
#       continue
#    print(char,end="")


player1 = input('Player 1 Enter the value: ')
player2 = input('Player 2 Enter the value: ')

rock ='Rock'
scissors ='Scissors'
paper = 'Paper'

if(player1==rock and player2==scissors):
    print('Player 1 is the winner!')
elif(player1==paper and player2==rock):
    print()
