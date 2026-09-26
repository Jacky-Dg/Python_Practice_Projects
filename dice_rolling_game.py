import random

# Global Variables
roll_message = "Roll the dice? (y/n): "
invalid_choice_message = "Invalid choice!"
thank_you_message = "Thanks for playing!"

def main():
    dice_game()

def dice_game():
    while True:
        user_choice = input(roll_message).lower()
        if user_choice == 'y':
            dice_roll_1 = random.randint(1, 6)
            dice_roll_2 = random.randint(1, 6)
            print(f"({dice_roll_1}, {dice_roll_2})")
        elif user_choice == 'n':
            print(thank_you_message)
            break
        else:
            print(invalid_choice_message)

main()
    