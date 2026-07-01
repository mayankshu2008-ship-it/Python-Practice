import random
def choose(rock, paper, scissor):
    return random.choice([rock, paper, scissor])
b = input('Choose rock, paper or scissor: ')
b = b.lower()
if b != 'rock' and b != 'paper' and b != 'scissor':
    print('Invalid input')
    exit()
a = choose('rock', 'paper', 'scissor')
if a == 'rock':
    print('The computer chose rock')
    if b == 'rock':
        print('It is a tie')
    elif b == 'paper':
        print('You win')
    else:
        print('You lose')
elif a == 'paper':
    print('The computer chose paper')
    if b == 'rock':
        print('You lose')
    elif b == 'paper':
        print('It is a tie')
    else:
        print('You win')
elif a == 'scissor':
    print('The computer chose scissor')
    if b == 'rock':
        print('You win')
    elif b == 'paper':
        print('You lose')
    else:
        print('It is a tie')
while True:
    a = input('Do you want to play again? (y/n): ')
    if a == 'y':
        b = input('Choose rock, paper or scissor: ')
        b = b.lower()
        if b != 'rock' and b != 'paper' and b != 'scissor':
            print('Invalid input')
            exit()

        a = choose('rock', 'paper', 'scissor')
        if a == 'rock':
            print('The computer chose rock')
            if b == 'rock':
                print('It is a tie')
            elif b == 'paper':
                print('You win')
            else:
                print('You lose')
        elif a == 'paper':
            print('The computer chose paper')
            if b == 'rock':
                print('You lose')
            elif b == 'paper':
                print('It is a tie')
            else:
                print('You win')
        elif a == 'scissor':
            print('The computer chose scissor')
            if b == 'rock':
                print('You win')
            elif b == 'paper':
                print('You lose')
            else:
                print('It is a tie')
    else:
        break

