import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 0 and 100. Can you guess what it is?")

min = int(input("Enter Zero: "))
max = int(input("Enter One hundred: "))

print(f"\nYou have 10 chances to guess the number between {min} and {max}. Let's start!")

num = random.randint(min, max)
chances = 10
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {guess_counter} attempts.')
        break

    elif guess_counter >= chances and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')