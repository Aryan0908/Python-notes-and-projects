import random
import number_guessing_art

print(number_guessing_art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
choosen_number = random.randint(1, 100)
print(choosen_number)
user_input = input("Choose a difficulty: Type 'Easy' or 'Hard' ").lower()
user_lives = 0

if user_input == "easy":
    user_lives = 10
elif user_input == "hard":
    user_lives = 5
else:
    print("Invalid input! Start Again.")

def game(number, lives):
    win = False
    while lives != 0 and win == False:
        print(f"\nYou have {lives} attempts remaining to guess the number")
        user_guess = int(input("Guess a number: "))
        if user_guess == number:
            win = True
            print(f"You Win! The number was {number}")
        elif user_guess > number:
            lives -= 1
            print("Too High\nGuess Again")
        elif user_guess < number:
            lives -= 1
            print("Too Low\nGuess Again")
    
    if lives == 0:
        print(f"\nYou ran out of guesses.\nYou Loose.\nThe number was {number}")




game(number=choosen_number, lives=user_lives)
