import os
import curses


from utils.dirlist import get_dir_list


icol = {
    'red': 1,
    'green': 2,
    'yellow': 3,
    'blue': 4,
    'magenta': 5,
    'cyan': 6,
    'white': 7,
}


def file_name_formatter(file_name: str, max_size: int = 15) -> str:
    file_name = file_name.ljust(max_size)
    if len(file_name) > max_size:
        return file_name[:max_size-3] + '...'
    else:
        return file_name


def path_finder_menu() -> str:
    def character(stdscr,) -> str:
        dir = os.getcwd() + '/'
        curses.init_pair(1, 7, curses.COLOR_BLACK)
        curses.init_pair(2, icol['green'], curses.COLOR_BLACK)
        curses.init_pair(3, icol['magenta'], curses.COLOR_BLACK)

        while True:
            dirlist = get_dir_list(dir)
            c = 0
            option = 0

            while True:
                stdscr.erase()

                stdscr.addstr(f"{dir}\n", curses.color_pair(3))

                for i in range(len(dirlist)):
                    if i == option:
                        attr = curses.color_pair(2)
                        stdscr.addstr(f'> ', attr)
                    else:
                        attr = curses.color_pair(1)
                        stdscr.addstr(f'  ', attr)
                        
                    stdscr.addstr(f'{file_name_formatter(dirlist[i])}' + '\n', attr)
                    # stat = os.stat(dirlist[i])
                    # print(stat, type(stat))
                    # os.path.getmtime()

                c = stdscr.getch()
                if c == curses.KEY_UP and option > 0:
                    option -= 1
                elif c == curses.KEY_DOWN and option < len(dirlist) - 1:
                    option += 1
                elif c == 10:
                    dir += dirlist[option]
                    break
                elif chr(c) in 'zZ' and dir.count('/') > 1:
                    dir = '/'.join(dir.split('/')[:-2]) + '/'
                    break
                elif chr(c) in 'qQ':
                    raise KeyboardInterrupt

            if os.path.isfile(dir):
                return dir
                
    return curses.wrapper(character)
