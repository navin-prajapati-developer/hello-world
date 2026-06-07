import random

number = random.randint(1, 10)
attempts = 0

print("Guess a number between 1 and 10!")

while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You got it in " + str(attempts) + " attempts!")
        break
