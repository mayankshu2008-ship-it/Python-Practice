# Snake, Water, Gun Game
import random

def computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def player_choice():
    choice = input('Enter your choice (snake, water, gun):').lower()
    if choice not in ['snake', 'water', 'gun']:
        print('Invalid Choice! Please choose again.')
        return player_choice()
    return choice
    
computer = computer_choice()
player = player_choice()
if computer == player:
    print('It\'s a tie!')
elif computer == 'snake' and player == 'water':
    print('Computer wins! Snake drinks water.')
elif computer == 'water' and player == 'gun':
    print('Computer wins! Water sinks gun.')
elif computer == 'gun' and player == 'snake':
    print('Computer wins! Gun kills snake.')
else:
    print('You win!')
print(f'Computer chose: {computer}')
print(f'You chose: {player}')
while True:
    a = input('Do you want to play again? (y/n): ')
    

    if a == 'y':
        computer = computer_choice()
        player = player_choice()
        
        if computer == player:
                print('It\'s a tie!')
        elif computer == 'snake' and player == 'water':
                print('Computer wins! Snake drinks water.')
        elif computer == 'water' and player == 'gun':
                print('Computer wins! Water sinks gun.')
        elif computer == 'gun' and player == 'snake':
                print('Computer wins! Gun kills snake.')
        else:
                print('You win!')
    elif a == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid input! Please enter y or n.')
