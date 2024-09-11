import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    
    while guess != number_to_guess:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Congratulations! You've guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guess_the_number()