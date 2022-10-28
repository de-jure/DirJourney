import sys
from getpass import getpass


def start() -> list:
    args = sys.argv
    login, password = None, None

    for i in range(len(args)):
        try: 
            if args[i] == '-l':
                login = args[i+1]
            elif args[i] == '-p':
                password = args[i+1]
        except IndexError:
            pass

    print('Welcome to DirJourney (by de_jure)')

    if not login or not password:
        print('Please authorize to continue')
        if not login:
            login = input('Login: ')
        if not password:
            password = getpass('Password: ')

    print(login, password)

    return login, password
