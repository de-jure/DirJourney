"""_summary_

Returns:
    _type_: _description_
"""
import sys
from getpass import getpass


def start() -> None:
    """_summary_

    Returns:
        list: _description_
    """
    args = sys.argv
    login, password = None, None

    for i, arg in enumerate(args):
        try:
            if arg == '-l':
                login = args[i+1]
            elif arg == '-p':
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
