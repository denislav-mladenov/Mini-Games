import random

print("Computer: Welcome to the number guessing game!")
print("Computer: I will pick a random number between 1 and 100.")
print("Computer: Can you guess it in 5 attempts?")

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Your guess: "))
    guesses += 1

    if guess < number:
        print("Computer: Too low, try again!")
    elif guess > number:
        print("Computer: Too high, try again!")
    else:
        print(f"Computer: You got it in {guesses} tries!")
        break