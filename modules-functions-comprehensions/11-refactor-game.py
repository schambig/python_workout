import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower() # Considerar si esque el ususario ingresa alguna mayuscula

    if user_option not in options:
        print('Esa opcion no es valida')
        print()
        # continue
        return None, None
    
    computer_option = random.choice(options)

    print('Seleccion de usuario =>', user_option)
    print('Seleccion de la compu =>', computer_option)

    return user_option, computer_option

def game_rules(user_option, computer_option, user_wins, computer_wins):
    # user_wins = 0
    # computer_wins = 0
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('gana el usuario!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('gana la compu!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('gana el usuario!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('gana la compu!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('gana el usuario!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('gana la compu!')
            computer_wins += 1

    return user_wins, computer_wins

def get_winner(user_wins, computer_wins):
    if user_wins == 2:
        print('El ganador del juego es el usuario')
        # quit() # Take a look at the NOTE at the EOF
        exit()        

    if computer_wins == 2:
        print('El ganador del juego es la compu')      
        # quit() # Take a look at the NOTE at the EOF
        exit()        


def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1
    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        user_option, computer_option = choose_options()
        user_wins, computer_wins = game_rules(user_option, computer_option, user_wins, computer_wins)
        get_winner(user_wins, computer_wins)
            
        rounds += 1
        print()

run_game()

# NOTE:
# Both quit() and exit() can be used to finish a function, but they have different implications.
# quit() is a built-in function that raises the SystemExit exception, which tells the Python interpreter to exit immediately.
# exit() is a function in the sys module that does the same thing.

# The main difference between the two is that:

# quit() is not always available.
# If the site module is not imported, then quit() will not be defined.
# This is because quit() was originally added to Python to make it more user-friendly.
# It is designed to be used in the interactive interpreter, where it is easy to type quit to exit.

# exit(), on the other hand, is always available.
# It is a built-in function, so it is always available in any Python program.
# This makes it a more reliable option for finishing a function.

# In general, it is best to use exit() to finish a function.
# It is more reliable and it is not tied to the interactive interpreter.
# However, if you are sure that the site module is imported, then you can use quit() as well.