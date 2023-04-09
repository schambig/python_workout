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
        quit() # is there a better way to end a loop? because break doesn't work outside a while loop
        
    if computer_wins == 2:
        print('El ganador del juego es la compu')      
        quit() # is there a better way to end a loop? because break doesn't work outside a while loop


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