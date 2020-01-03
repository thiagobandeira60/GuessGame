import random

# In this guess game, we are also trying to keep track of the number of attempts.
# That's why the variable guess, which is the player's input, is initialized as 0.
# The c variable is to count the number of attempts ,and needs to be initialized as 0 as well.

print('Welcome to the guess game!')
num = random.randint(1,9)
guess = 0
c = 0

# The game is running.
# The player will be asked to continue playing or not.

while True:
    guess = int(input('Guess a number between 1 and 9: '))

    # We keep incrementing c as the game goes on.
    c += 1
    if guess < num:
        print('You guessed too low!')
        if str(input('Do you want to guess again? Enter yes or no:\n')) == 'yes':
            continue
        else:
            print('End game.')
            break
    elif guess > num:
        print('You guessed too high!')
        if str(input('Do you want to guess again? Enter yes or no:\n')) == 'yes':
            continue
        else:
            print('End game.')
            break
    else:

        # When the player gets the right number, it shows the number of attempts that were incremented in c.
        print('You got it! That is the exact number.')
        print('You took', c, 'tries!')
        break
