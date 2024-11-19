from builtins import Exception, input, int, print, range
import requests
import random
from Score import add_score
final_rate = 0


def get_money_interval(difficulty):
    try:
        global final_rate
        # Get the ILS Value from API request.
        url = 'http://data.fixer.io/api/latest?access_key=0f6a584b7f1d9f23c37a6c5ca23f804c&format=1'
        req = requests.get(url)
        json_data = req.json()

        # Get the ILS Value from API response.
        ils_rate = json_data['rates']['ILS']

        # the input of the random number
        random_number = random.randint(1, 100)
        final_rate = (random_number - (5 - difficulty),
                      ils_rate + (5 - difficulty))

    except Exception as error:
        print(error)


def get_guess_from_user(final_rate):
    guess_input = int(input('Please enter a guess of your amount of USD : '))
    is_between = guess_input in range(final_rate[0], int(final_rate[1]))
    if(is_between):
        return True
    else:
        return False


def play_currencies_game(difficulty):
    get_money_interval(difficulty)
    tuplie_to_list = list(final_rate)
    if(get_guess_from_user(tuplie_to_list)) == True:
        add_score(difficulty)
        print('Your gussing is correct!')
    else:
        print('Your gussing is not correct!')
