
#Thai-Son Nguyen's decode function
def decode(password):
    password = str(password)  #in case something other than a string is passed in
    decoded_password = ""
    for num in password:
        decoded_digit = int(num) - 3
        decoded_password += str(decoded_digit)
    return decoded_password


