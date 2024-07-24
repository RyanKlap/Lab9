
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')

if __name__ == '__main__':
    while True:
        menu()
        option = input('Please enter an option: ')

        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!')
            print('')

        if option == '2':
            decoded_pass = decode(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
            print('')

        if option == '3':
            break

