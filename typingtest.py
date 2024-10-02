# Create a terminal-based interface for user efficiency using curses module
import curses  

# Initialize and clean up the environment 
from curses import wrapper

# Add a welcoming remark string as a start off of the test
# Ask for the user's response to start the game by typing any key to begin (/n) is used to move this on the next line
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Red’s Typing Test! Practice your typing and break your own speed limit!") 
    stdscr.addstr("\nPress any key to begin!")      # Prompt the user to start the test
    stdscr.refresh()                                # Refresh the screen to show the added text
    stdscr.getkey ()   
    
# Display the target text for the typing test, clear the screen, and wait for user input.    
def wpm_test(stdscr): 
    target_text = "Hi! This is just some text for this test"     #Load the target text
    current_text = []                              # Initialize an empty list for the user's input

    stdscr.clear()
    stdscr.addstr(target_text)     
    stdscr.refresh()                               # Refresh the screen to show the added text

#Create a while loop to continuously run the typing test
    while True:
        stdscr.clear()                                        #Clear the screen at the beginning of each loop iteration
        stdscr.addstr(target_text)                  


        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()
   
#If the user presses the ESC key (ASCII value 27), exit the loop and program
        if ord(key) == 27:           #27 is the ASCII code for ESC
            break

#If the user presses backspace, remove the last typed character
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:      #Ensure there's text to delete
                current_text.pop()         #Remove the last character from current_text

        else:       
            current_text.append(key)       #Append what they type to the current text

        stdscr.refresh()                   #Refresh the screen to show updates

                        
# Main function initializes the color pairs 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)



wrapper(main)