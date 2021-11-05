import random
correctNumber = random.randint(1,10)
guess = int(input('Please enter a number between 1 and 10:'))
while guess != correctNumber:
    if guess > correctNumber:
        print('Your guess is greater than the correct number. Try again:')
        guess = int(input())
    elif guess < correctNumber:
        print('Your guess is smaller than the correct number. Try again:')
        guess = int(input())
print('Congrats! Your guess is correct.')
