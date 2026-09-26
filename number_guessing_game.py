import random

# Global Variables
high_message = "Too high!"
low_message = "Too low!"
correct_message = "Congratulations! You guessed the number."

invalid_message = "Please enter a valid number"
guess_message = "Guess the number between 1 and 100: "

higher_range = 100
lower_range = 1

def main():
    number_guesser_v1()

def number_guesser_v1():
    number = random.randint(lower_range, higher_range)

    while True:
        user_guess = get_user_guess()

        if is_user_correct(user_guess, number):
            break

def get_user_guess():
    while True:
        user_guess = input(guess_message)
        if user_guess.isdigit():
            return user_guess
        else:
            print(invalid_message)

def is_user_correct(user_guess, number):
    if int(user_guess) > number:
        print(high_message)
    elif int(user_guess) < number:
        print(low_message)
    else:
        print(correct_message)
        return True
    return False

def number_guesser_v2():
    number = random.randint(lower_range, higher_range)

    while True:
        try:
            user_guess = int(input(guess_message))

            if int(user_guess) > number:
                print(high_message)
            elif int(user_guess) < number:
                print(low_message)
            else:
                print(correct_message)
                break
        except ValueError:
            print(invalid_message)

main()