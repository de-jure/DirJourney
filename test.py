
# import curses

# screen = curses.initscr()

# # Update the buffer, adding text at different locations
# screen.addstr(0, 0, "This string gets printed at position (0, 0)")
# screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
# screen.addstr(4, 4, "X")
# screen.addch(5, 5, "Y")

# # Changes go in to the screen buffer and only get
# # displayed after calling `refresh()` to update
# screen.refresh()

# curses.napms(3000)
# curses.endwin()

# import curses

# screen = curses.initscr()

# screen.addstr("Hello, I will be cleared in 2 seconds.")
# screen.refresh()
# curses.napms(2000)

# # Wipe the screen buffer and set the cursor to 0,0
# screen.clear()

# screen.refresh()
# curses.napms(2000)

# curses.endwin()

# import curses
# import subprocess
# import os

# # Create a screen and print hello
# screen = curses.initscr()
# screen.addstr("Hello! Dropping you in to a command prompt...\n")
# print("Program initialized...")
# screen.refresh()
# curses.napms(2000)

# # Hide the screen, show original terminal, restore cursor position
# curses.endwin()

# # Update screen in background
# screen.addstr("I'll be waiting when you get back.\n")

# # Drop the user in a command prompt
# print("About to open command prompt...")
# curses.napms(2000)

# if os.name == 'nt':
#     shell = 'cmd.exe'
# else:
#     shell = 'sh'
# subprocess.call(shell)

# # When the subprocess ends, return to our screen.
# # also restoring cursor position
# screen.refresh()
# curses.napms(2000)

# # Finally go back to the terminal for real
# curses.endwin()

# import curses

# screen = curses.initscr()
# num_rows, num_cols = screen.getmaxyx()
# curses.endwin()

# print("Rows:    %d" % num_rows)
# print("Columns: %d" % num_cols)

# import curses

# screen = curses.initscr()
# screen.addstr("Press any key...")
# screen.refresh()

# c = screen.getch()

# curses.endwin()

# # Convert the key to ASCII and print ordinal value
# print("You pressed %s which is keycode %d." % (chr(c), c))

# import os
# dir_list = os.listdir('.')
 
# print("Files and directories in '", path, "' :")
 
# prints all files
# print(dir_list)

# import os, sys
# from curses import panel, initscr


# x = os.system('ls -l')
# print(type(x))
# print(x)
# help(panel)


# screen = initscr()
# help(screen)
# panel.top_panel()



# ''.endswith()




