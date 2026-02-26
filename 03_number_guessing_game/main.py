import random

print("Welcome to the Guessing Game!")
print("Choose a mode:")
print("1. You guess the computer's number")
print("2. Computer guesses your number")

choice = input("Enter 1 or 2: ")

#User guessing
if choice == "1":
    lowest_num = 1
    highest_num = 100

    number = random.randint(lowest_num, highest_num)
    guess = 0

    print("I have picked a number between 1 and 100. Try to guess it!")

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < number:
            print("Guess higher!")
        elif guess > number:
            print("Guess lower!")
        else:
            print("You won! 🎉")


#computer guessing

elif choice == "2":
    print("Think of a number between 1 and 100 and I will try to guess it!")

    lowest = 1
    highest = 100

    guess = random.randint(lowest, highest)
    feedback = input(f"My guess is {guess}. Is it 'higher', 'lower', or 'correct'? ").lower()

    while feedback != "correct":

        while feedback not in ["higher", "lower", "correct"]:
            feedback = input("Please type only: higher, lower, or correct: ").lower()

        if feedback == "higher":
            lowest = guess + 1
        elif feedback == "lower":
            highest = guess - 1

        guess = random.randint(lowest, highest)
        feedback = input(f"My new guess is {guess}. Is it 'higher', 'lower', or 'correct'? ").lower()

    print("Yay! The computer guessed your number 😄")


else:
    print("Invalid choice. Please restart and enter 1 or 2.")