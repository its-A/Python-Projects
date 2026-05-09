import random

print("Number Guessing Game. You have 10 attempts to guess the number between 1 and 100.")

lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

print("You have 7 chances to guess the number between", lower_bound, "and", upper_bound)

num=random.randint(lower_bound, upper_bound)
attempts = 7
guesses = 0

while guesses < attempts:
    guesses += 1
    guess = int(input("Enter your guess: "))

    if guesses == num:
        print("Congratulations! You've guessed the number in", guesses, "attempts.")
        break
    elif guess < num and guesses != attempts:
        print("Your guess is too low. Try again.")  
    elif guess > num:
         print("Your guess is too high. Try again.")
    elif guesses < attempts:
        print("Sorry, you've used all your attempts. The number was", num)