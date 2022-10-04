import time

number = int(input("Enter a number between 1 and 10. I'll try to guess it.  "))

number_of_guesses = 0

high = 10

low = 1

guess = 0

while guess != number:
    guess = (low + high) // 2
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