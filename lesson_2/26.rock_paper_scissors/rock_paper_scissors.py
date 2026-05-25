import random
import os
import time
import json

with open('26.rock_paper_scissors/messages.json', 'r') as file:
    messages = json.load(file)

MOVES = {
    'rock': { 'abbreviation': 'r', 'beats': ['scissors', 'lizard']},
    'lizard': { 'abbreviation': 'l', 'beats': ['spock', 'paper']},
    'spock': { 'abbreviation': 'sp', 'beats': ['scissors', 'rock']},
    'paper': { 'abbreviation': 'p', 'beats': ['spock', 'rock']},
    'scissors': { 'abbreviation': 'sc', 'beats': ['paper', 'lizard']}
  }


counter = {'user': 0 , 'computer': 0}
MAX_POINTS = 3

def prompt(message):
    print(f"==> {message}")

def get_choice(user_string):
    user_string = user_string.lower().strip()

    if user_string.startswith(MOVES['rock']['abbreviation']):
        return 'rock'
    if user_string.startswith(MOVES['scissors']['abbreviation']):
        return 'scissors'
    if user_string.startswith(MOVES['spock']['abbreviation']):
        return 'spock'
    if user_string.startswith(MOVES['lizard']['abbreviation']):
        return 'lizard'
    if user_string.startswith(MOVES['paper']['abbreviation']):
        return 'paper'
    return False

def player_wins(player_choice, computer):
    return computer in MOVES[player_choice]['beats']

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
        prompt(f"You are the max winner, you obtained {point['user']} points "
        f"and the computer obtained {point['computer']} points")

    if point['computer'] == MAX_POINTS:
        prompt(f"Computer is the max winner, you obtained {point['user']} "
        f"points and the computer obtained {point['computer']} points")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_validated_choice():
    user_answer = input()
    transform_answer = get_choice(user_answer)

    while transform_answer not in MOVES :
        prompt(messages['not_valid'])
        user_selection = input()
        transform_answer = get_choice(user_selection)

    return transform_answer

def play_again():
    while True:
        prompt(messages["another_game?"])
        answer = input().lower().strip()
        if answer.startswith('y') or  answer.startswith('n'):
            return  answer.startswith('y')

        prompt(messages['not_valid'])

def play_one_round():

    prompt(f'Choose one: {', '.join(list(MOVES))} '
            'you can write just the first letters')

    choice = get_validated_choice()
    computer_choice = random.choice(list(MOVES))

    prompt(f'You chose {choice}, the computer chose {computer_choice}')
    display_winner(choice, computer_choice)

    if player_wins(choice, computer_choice):
        counter['user'] += 1
    elif choice != computer_choice:
        counter['computer'] +=1

    prompt(f'Current score - You: {counter['user']} '
            f'Computer: {counter['computer']} ')

clear_screen()
prompt(messages["welcome"])

while True:
    play_one_round()

    time.sleep(2)
    clear_screen()

    if game_ends(counter):
        display_max_winner(counter)

        if not play_again():
            break

        counter = {'user': 0 , 'computer': 0}

        