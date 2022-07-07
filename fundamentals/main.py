user_option = input('piedra, papel o tijera => ')
computer_option = 'tijera'

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('gana el usuario!')
    else:
        print('papel gana a piedra')
        print('gana la compu!')