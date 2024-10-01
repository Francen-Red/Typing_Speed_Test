# Create a terminal-based interface for user efficiency using curses module
import curses  

# Initialize and clean up the environment 
from curses import wrapper

#Add a welcoming remark string as a start off of the test
#Ask for the user's response to start the game by typing any key to begin (/n) is used to move this on the next line
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Red’s Typing Test! Practice your typing and break your own speed limit!") 
    stdscr.addstr("\nPress any key to begin!")      #Prompt the user to start the test
    stdscr.refresh()                                #Refresh the screen to show the added text
    stdscr.getkey ()   
    

# Setting up the standard screen for outputrd
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr("Hiii! This is just some text for this test!", curses.color_pair(2)) 
    stdscr.refresh()                              
    key = stdscr.getkey () 
    print(key) 

wrapper(main)