import random
import time

number = int(input("Enter a number between 1 and 10. I'll try to guess it in 3 tries."))

number_of_guesses = 0

while number_of_guesses < 3:
    guess = random.randint(1, 10)
    number_of_guesses += 1
    if guess > number:
        print(guess)
        print('Nope. That was not it.')
    if guess < number:
        print(guess)
        print('Nope. That was not it.')
    if guess == number:
        print(guess)
        break
    time.sleep(1)

if guess == number:
    print('I guessed the number in', number_of_guesses, 'tries!')
else:
    print('I did not guess the number.')