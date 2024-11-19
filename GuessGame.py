# importing the random module
import random
from Score import add_score
secret_number = 0
flag = False

def generate_number(difficulty):
    global secret_number
    secret_number = random.randint(1, difficulty)
    print(secret_number)

def get_guess_from_user():
    guess_number = int(input("Please enter the guess number "))
    compare_results(guess_number)


def compare_results(guess_number):
    global flag
    if guess_number == secret_number:
        flag = True
    else:
        flag = False

def play_guess_game(game_difficulty):
    generate_number(game_difficulty)
    get_guess_from_user()

    if flag:
        print('You\'re gussing right!' )
        add_score(game_difficulty)
    else:
         print('You\'re gussing not right!' )
