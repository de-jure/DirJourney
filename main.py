import os
from ui.path_finder_menu import path_finder_menu

if __name__ == '__main__':
    try: 
        file_path = path_finder_menu()
        os.system(f'cat {file_path}')
    except KeyboardInterrupt:
        pass
