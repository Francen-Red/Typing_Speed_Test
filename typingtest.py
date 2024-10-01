# Create a terminal-based interface for user efficiency using curses module
import curses  

# Initialize and clean up the environment 
from curses import wrapper

# Setting up the standard screen for output
def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hiii! This is just some text for this test!") 
    stdscr.refresh()                              
    stdscr.getkey ()  