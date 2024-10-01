# Create a terminal-based interface for user efficiency using curses module
import curses  

# Initialize and clean up the environment 
from curses import wrapper

# Setting up the standard screen for output
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.clear()
    stdscr.addstr("Hiii! This is just some text for this test!", curses.color_pair(2)) 
    stdscr.refresh()                              
    stdscr.getkey ()  

wrapper(main)