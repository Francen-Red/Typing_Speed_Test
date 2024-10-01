# Create a terminal-based interface for user efficiency using curses module
import curses  

# Initialize and clean up the environment 
from curses import wrapper

# Add a welcoming remark string as a start off of the test
# Ask for the user's response to start the game by typing any key to begin (/n) is used to move this on the next line
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Red’s Typing Test! Practice your typing and break your own speed limit!") 
    stdscr.addstr("\nPress any key to begin!")      #Prompt the user to start the test
    stdscr.refresh()                                #Refresh the screen to show the added text
    stdscr.getkey ()   
    
# Display the target text for the typing test, clear the screen, and wait for user input.    
def wpm_test(stdscr): 
    target_text = "Hi! This is just some text for this test"     #Load the target text
    current_text = []                              #Initialize an empty list for the user's input

    stdscr.clear()
    stdscr.addstr(target_text)     
    stdscr.refresh()                                #Refresh the screen to show the added text
    stdscr.getkey ()   
    




# Main function initializes the color pairs 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)



wrapper(main)