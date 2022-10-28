"""_summary_

Raises:
    KeyboardInterrupt: _description_

Returns:
    _type_: _description_
"""
import os
import curses


from utils.dirlist import get_dir_list
from core.filename_formatter import filename_formatter
from config import PATH_TEXT_COLOR, PATH_BACKGROUND_COLOR
from config import UNPICKED_LINE_TEXT_COLOR, UNPICKED_LINE_BACKGROUND_COLOR
from config import PICKED_LINE_TEXT_COLOR, PICKED_LINE_BACKGROUND_COLOR


def path_finder_menu() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    def character(stdscr,) -> str:
        path = os.getcwd() + '/'
        curses.init_pair(1, PATH_TEXT_COLOR, PATH_BACKGROUND_COLOR)
        curses.init_pair(2, UNPICKED_LINE_TEXT_COLOR, UNPICKED_LINE_BACKGROUND_COLOR)
        curses.init_pair(3, PICKED_LINE_TEXT_COLOR, PICKED_LINE_BACKGROUND_COLOR)

        while True:
            dirlist = get_dir_list(path)
            pressed_key = 0
            option = 0

            while True:
                stdscr.erase()

                stdscr.addstr(f"{path}\n", curses.color_pair(1))

                for i, entity in enumerate(dirlist):
                    if i == option:
                        attr = curses.color_pair(3)
                        stdscr.addstr('> ', attr)
                    else:
                        attr = curses.color_pair(2)
                        stdscr.addstr('  ', attr)

                    stdscr.addstr(f'{filename_formatter(entity)}' + '\n', attr)
                    # stat = os.stat(dirlist[i])
                    # print(stat, type(stat))
                    # os.path.getmtime()

                pressed_key = stdscr.getch()
                if pressed_key == curses.KEY_UP and option > 0:
                    option -= 1
                elif pressed_key == curses.KEY_DOWN and option < len(dirlist) - 1:
                    option += 1
                elif pressed_key == 10:
                    path += dirlist[option]
                    break
                elif chr(pressed_key) in 'zZ' and path.count('/') > 1:
                    path = '/'.join(path.split('/')[:-2]) + '/'
                    break
                elif chr(pressed_key) in 'qQ':
                    raise KeyboardInterrupt

            if os.path.isfile(path):
                return path

    return curses.wrapper(character)
