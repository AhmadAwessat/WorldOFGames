from MemoryGame import play_memory_game
from GuessGame import play_guess_game
from CurrencyRouletteGame import play_currencies_game

# text for input
choose_game_text = 'Please choose a game to play from 1 to 3: '
choose_game_difficulty_text = 'Please choose a game difficulty from 1 to 5:'

# Welcome function
def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'

# Load Game function
def load_game():

    print('--------------------------------------------------------------')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print('2. Guess Game - guess a number and see if you chose like the computer')
    print('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
    print('--------------------------------------------------------------')

    game_arr = ['1', '2', '3']
    difficulty_arr = ['1', '2', '3', '4', '5']
    play_game = input(choose_game_text)
    while play_game not in game_arr:
        play_game = input(choose_game_text)
    game_difficulty = input(choose_game_difficulty_text)
    while game_difficulty not in difficulty_arr:
        game_difficulty = input(choose_game_difficulty_text)
    if(play_game=='1'):
        play_guess_game(int(game_difficulty))
        pass
    elif(play_game=='2'):
        play_memory_game(int(game_difficulty))
    else:
        play_currencies_game(int(game_difficulty))

