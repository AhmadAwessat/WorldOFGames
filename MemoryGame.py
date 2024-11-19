import random
import time
import os
from Utils import screen_cleaner
from Score import add_score

randomlist = []
list_guess = []

def generate_sequence(difficulty):
    time.sleep(0.7)
    for i in range(0,difficulty):
        n = random.randint(1,101)
        randomlist.append(n)
    
    print(randomlist)
    
    # wait then clear
    time.sleep(5)
    screen_cleaner()
    
def get_list_from_user(difficulty):
    global list_guess 
    list_guess = [None] * difficulty 
    for i in range(0,len(list_guess)):
        guess_number = int(input(f"Please enter the {i+1} guess number "))
        list_guess[i] = guess_number
        print(f'{list_guess}')

def is_list_equal(list_guess):
    if list_guess == randomlist:
        return True
    else:
        return False

def play_memory_game(difficulty):
    global list_guess
    generate_sequence(difficulty)
    get_list_from_user(difficulty)
    if(is_list_equal(list_guess)==True):
        print('You won!')
        add_score(difficulty)
    else:
        print('You Lose... try again!')
