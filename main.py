# Main - Ryan Klapmeyer

def encode(passcode):
    pass_list = list(passcode)
    encode_list = []
    for i in range(len(pass_list)):
        if int(pass_list[i]) < 7:
            pass_list[i] = int(pass_list[i]) + 3
            encode_list.append(pass_list[i])
        else:
            pass_list[i] = (int(pass_list[i]) + 3) - 10
            encode_list.append(pass_list[i])

    encode_str = ''
    for i in range(len(encode_list)):
        encode_str += str(encode_list[i])

    return encode_str

def decode(passcode):
    pass_list = list(passcode)
    decode_list = []
    for i in range(len(pass_list)):
        if int(pass_list[i]) < 3:
            pass_list[i] = int(pass_list[i]) + 7
            decode_list.append(pass_list[i])
        else:
            pass_str = int(pass_list[i]) - 3
            decode_list.append(pass_str)

    decode_str = ''
    for i in range(len(decode_list)):
        decode_str += str(decode_list[i])

    return decode_str

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
