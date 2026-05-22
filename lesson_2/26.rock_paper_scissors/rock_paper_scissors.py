import random
import os
import time

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
counter = {'user': 0 , 'computer': 0}
WINING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors'],
}
MAX_POINTS = 3

def prompt(message):
    print(f"==> {message}")

def get_choice(user_string):
    user_string = user_string.lower().strip()

    if user_string.startswith('r'):
        return 'rock'
    if user_string.startswith('sc'):
        return 'scissors'
    if user_string.startswith('sp'):
        return 'spock'
    if user_string.startswith('l'):
        return 'lizard'
    if user_string.startswith('p'):
        return 'paper'
    return False


def player_wins(player_choice, computer):
    return computer in WINING_COMBOS[player_choice]

def display_winner(play_choice, computer):
    if player_wins(play_choice, computer):
        prompt('You win!')
    elif play_choice == computer:
        prompt("It's a tie!")
    else:
        prompt('Computer wins!')

def game_ends(points):
    return  MAX_POINTS in (points['user'], points['computer'])

def display_max_winner(point):
    if point['user'] == MAX_POINTS:
        prompt(f'You are the max winner, you obtained {point['user']} points '
        f'and the computer obtained {point['computer']} points')

    if point['computer'] == MAX_POINTS:
        prompt(f'Computer is the max winner, you obtained {point['user']} '
        f'points and the computer obtained {point['computer']} points')

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_validated_choice(user_answer):

    while user_answer not in VALID_CHOICES :
        prompt("That's not a valid choice, please try again")
        user_selection = input()
        user_answer = get_choice(user_selection)

    return user_answer

clear_screen()
prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock')
while True:
    prompt(f'Choose one: {', '.join(VALID_CHOICES)} '
            'you can write just the first letters')

    user_choice = input()
    choice = get_choice(user_choice)

    choice = get_validated_choice(choice)

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, the computer chose {computer_choice}')
    display_winner(choice, computer_choice)

    if player_wins(choice, computer_choice):
        counter['user'] += 1
    elif choice != computer_choice:
        counter['computer'] +=1

    prompt(f'Current score - You: {counter['user']} '
            f'Computer: {counter['computer']} ')
    time.sleep(2)
    clear_screen()

    if game_ends(counter):
        display_max_winner(counter)
        prompt('Do you want to play another game? ( y/n )')
        answer = input().lower().strip()

        while True:
            if answer.startswith('y') or  answer.startswith('n'):
                break

            prompt("That's not a valid answer")
            prompt('Do you want to play another game? ( y/n )')
            answer = input().lower().strip()

        counter = {'user': 0 , 'computer': 0}

        if answer[0] == 'n':
            break
