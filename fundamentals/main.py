import random

options = ('piedra', 'papel', 'tijera')

while True:

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower() # Considerar si esque el ususario ingresa alguna mayuscula
    
    if user_option not in options:
        print('Esa opcion no es valida')
    
    computer_option = random.choice(options)
    
    print('Seleccion de usuario', user_option)
    print('Seleccion de la compu', computer_option)
    
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('gana el usuario!')
        else:
            print('papel gana a piedra')
            print('gana la compu!')
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('gana el usuario!')
        else:
            print('tijera gana a papel')
            print('gana la compu!')
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('gana el usuario!')
        else:
            print('piedra gana a tijera')
            print('gana la compu!')