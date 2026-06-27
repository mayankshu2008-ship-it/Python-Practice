
import random
number = random.randint(1, 10)
a = int(input('Guess a number between 1 and 10: '))
while number != a:
    print('You guessed it wrong, try again')
    a = int(input('Guess a number between 1 and 10: '))
    if number == a:
     print('You guessed it right')
    elif a < number:
        print('Your guess is too low')
    elif a > number:
        print('Your guess is too high')

     
   
