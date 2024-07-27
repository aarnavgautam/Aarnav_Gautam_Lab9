from decode import decode
from encode import encode


def main():
    menu = '''Menu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: '''
    encoded_password = ''
    while True:
        option = int(input(menu))
        match option:
            case 1:
                password = str(input('Please enter your password to encode: '))
                encoded_password = encode(password)
                print('Your password has been encoded and stored!')
            case 2:
                print(f'The encoded password is {encoded_password}, and the original password '
                      f'is {decode(encoded_password)}.')
            case 3:
                break


if __name__ == '__main__':
    main()
