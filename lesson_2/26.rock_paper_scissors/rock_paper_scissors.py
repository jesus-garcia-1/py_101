import random


# rock wins scsissors
# rock wins lizard
# lizard wins paper
# lizard wins spock
# paper wins rock
# paper wins spock
# scissors wins paper
# scissor wins lizard
# spock wins rock
# spock wins scissors

# We want to add points to the computer_counter and user_counter, however
# they are global variables ??

# I want  a function that checks if winner is computer or the user

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
    if user_string.lower().startswith('r'):
        return 'rock'
    if user_string.lower().startswith('sc'):
        return 'scissors'
    if user_string.lower().startswith('sp'):
        return 'spock'
    if user_string.lower().startswith('l'):
        return 'lizard'
    if user_string.lower().startswith('p'):
        return 'paper'
    return False


def player_wins(player_choice, computer):
    return computer in WINING_COMBOS[player_choice]

def tie(player_choice, computer):
    return player_choice == computer

def add_points(player, computer):
    if player_wins(player, computer):
        counter['user'] += 1
    elif not tie(player, computer):
        counter['computer'] +=1

def display_winner(play_choice, computer):
    if player_wins(play_choice, computer):
        prompt('You win!')
    elif tie(play_choice, computer):
        prompt("It's a tie!")
    else:
        prompt('Computer wins!')

def game_ends(points):
    return  MAX_POINTS in (points['user'], points['computer'])

def display_max_winner(point):
    if point['user'] == MAX_POINTS:
        prompt(f'''You are the max winner, you obtained {point['user']} points
        and the computer obtained {point['computer']} points''')

    if point['computer'] == MAX_POINTS:
        prompt(f'''Computer is the max winner, you obtained {point['user']}
        points and the computer obtained {point['computer']} points''')

while True:
    prompt(f'''Choose one: {', '.join(VALID_CHOICES)},
    you can write just the first letters''')

    user_choice = input()
    choice = get_choice(user_choice)

    while choice not in VALID_CHOICES :
        prompt("That's not a valid choice, please try again")
        user_choice = input()
        choice = get_choice(user_choice)

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, the computer chose {computer_choice}')

    display_winner(choice, computer_choice)
    add_points(choice, computer_choice)

    while True:
        prompt('Do you want to play another game? ( y/n )')
        answer = input().lower()

        if answer.startswith('y') or answer.startswith('n'):
            break

        prompt("That's not a valid answer")

    if answer[0] == 'n':
        break

    if game_ends(counter):
        display_max_winner(counter)
        break
