import random

RPS_MESSAGE = "Rock, paper, or scissors? (r/p/s): "
LOSE_MESSAGE = "You lose"
WIN_MESSAGE = "You win"
TIE_MESSAGE = "You tie"
INVALID_MESSAE = "Invalid choice!"

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = { ROCK: '🪨', 
           SCISSORS: '✂️', 
           PAPER: '📄' }
choices = tuple(emojis.keys())

def main():
    play_rps_game()

def play_rps_game():
    while(True):
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

def get_user_choice():
    while True:
        user_choice = input(RPS_MESSAGE).lower()
        if user_choice in choices:
            return user_choice
        else:
            print(INVALID_MESSAGE)

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(TIE_MESSAGE)
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print(WIN_MESSAGE)
    else:
        print(LOSE_MESSAGE)


main()