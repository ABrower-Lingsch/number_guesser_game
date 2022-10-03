import random
import time

option = int(input('Enter "1" if you would like to guess the number. Enter "2" if you want me to guess the number. Enter any other key to exit.  '))

if option == 1:
    number = random.randint(1, 10)

    number_of_guesses = 0

    print('I am thinking of a number between 1 and 10. You get 3 guesses.')

    while number_of_guesses < 3:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low.')
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break

    if guess == number:
        print('You guessed the number in ', number_of_guesses, 'tries!')
    else:
        print('You did not guess the number. The number was ', number)

elif option == 2:
    number = int(input("Enter a number between 1 and 10. I'll try to guess it.  "))

    number_of_guesses = 0

    high = 10

    low = 1

    guess = 0

    while guess != number:
        guess = random.randint(low, high)
        number_of_guesses += 1
        if guess > number:
            high = guess - 1
            print(guess)
            print('That guess was too high.')
        if guess < number:
            low = guess + 1
            print(guess)
            print('That guess was too low.')
        time.sleep(1)
    else:
        print(guess)
        print('I guessed it right in', number_of_guesses, 'tries!')

elif option != 1 & option != 2:
    print('Please enter "1" or "2".')