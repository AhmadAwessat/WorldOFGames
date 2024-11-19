from Live import load_game, welcome

#call welcome function
name = input('Please enter your name :')
print('----------------------------------------------------------------')
print(welcome(name))

#start the game
load_game()