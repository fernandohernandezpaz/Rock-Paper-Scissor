# this program work with python 3
from random import randint

choices = ['rock', 'paper', 'scissors']


def main(message='Welcome to the Rock, Paper and Scissors Game'):
    computer = choices[randint(0, 2)]
    print('{}\n'.format(message))
    player = input('Your choice: ').lower()

    if player not in choices:
        main('Wrong answer, try again')

    print('Computer chose: {}'.format(computer))
    if player == computer:
        print('Draw')
    elif player == 'rock' and computer == 'paper':
        print('Computer wins')
    elif player == 'rock' and computer == 'scissors':
        print('You win')
    elif player == 'paper' and computer == 'scissors':
        print('Computer wins')
    elif player == 'paper' and computer == 'rock':
        print('You win')
    elif player == 'scissors' and computer == 'paper':
        print('You win')
    elif player == 'scissors' and computer == 'rock':
        print('Computer wins')


main()
