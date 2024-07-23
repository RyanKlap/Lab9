# Ryan Klapmeyer - Decode

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
