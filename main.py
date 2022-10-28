#!/usr/bin/env python3
import os
from ui.path_finder_menu import path_finder_menu
from formats import get_file_editor


if __name__ == '__main__':
    try:
        file_path = path_finder_menu()
        editor = get_file_editor(file_path)
        os.system(f'{editor} {file_path}')
    except KeyboardInterrupt:
        pass
