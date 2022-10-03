import random

number = random.randint(1, 10)

number_of_guesses = 0

print('I am thinking of a number between 1 and 10.')

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