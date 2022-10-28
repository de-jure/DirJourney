"""Configuration file for DirJourney by de_jure
"""
import curses


FILENAME_MAX_LEN = 20

# Theme
PATH_TEXT_COLOR = curses.COLOR_MAGENTA
PATH_BACKGROUND_COLOR = curses.COLOR_BLACK
PICKED_LINE_TEXT_COLOR = curses.COLOR_GREEN
PICKED_LINE_BACKGROUND_COLOR = curses.COLOR_BLACK
UNPICKED_LINE_TEXT_COLOR = curses.COLOR_WHITE
UNPICKED_LINE_BACKGROUND_COLOR = curses.COLOR_BLACK

FORMATS = {
    # "format": "editor",
    "py": "cat",
    "else": "cat", # default editor
}
