# This is a guess the number game
import random

secretNumber = random.randint(0,20)
print('I think the number is between 0 and 20.')

for guessesTaken in range(7):
	print('Guess a number.')
	guess = int(input())
	if guess > secretNumber:
		print('guess is too high')
	elif guess < secretNumber:
		print('guess is too low')
	else:
		break

if guess == secretNumber:
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Nope. The number I was thinking of was ' + str(secretNumber))

