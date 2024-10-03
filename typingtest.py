# Create a terminal-based interface for user efficiency using curses module
import curses  

# Initialize and clean up the environment 
from curses import wrapper

# Use the time module for easier calculation of WPM
import time



# Add a welcoming remark string as a start off of the test
# Ask for the user's response to start the game by typing any key to begin (/n) is used to move this on the next line
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Red’s Typing Test! Practice your typing and break your own speed limit!") 
    stdscr.addstr("\nPress any key to begin!")      # Prompt the user to start the test
    stdscr.refresh()                                # Refresh the screen to show the added text
    stdscr.getkey ()                                # Once a key is pressed the program will move on
    
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)                           # Display the target text  
    stdscr.addstr(1, 0, f"WPM: {wpm}")                           

    for i, char in enumerate(current):
        correct_char = target[i]                    # Get the corresponding character from the target text
        color = curses.color_pair(1)                # Green color for correct characters
        if char != correct_char:                    # If the character is incorrect
            color = curses.color_pair(2)            # Change color to red 

        stdscr.addstr(0, i, char, color)            # Display the character at row 0, column i with the determined color

     
# Display the target text for the typing test, clear the screen, and wait for user input.    
def wpm_test(stdscr): 
    target_text = "Hi! This is just some text for this test"     #Load the target text
    current_text = []                              # Initialize an empty list for the user's input
    wpm = 0                                        # Set WPM to 0 for starting the typing test 
    start_time = time.time()                       #Record the start time
    stdscr.nodelay(True)                           #Set getkey() to non-blocking mode to allow continuous updates

    
#Create a while loop to continuously run the typing test
    while True:
        time_elapsed = max(time.time() - start_time, 1)       # Calculate elapsed time, ensuring it's at least 1 second to avoid division by zero
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)       # Calculation of WPM

        stdscr.clear()                                        # Clear the screen at the beginning of each loop iteration
        display_text(stdscr, target_text, current_text, wpm)  # Display the target text and user input with WPM
        stdscr.refresh()                                      # Refresh the screen to show updated content


        try:
            key = stdscr.getkey()                             #Get the user's key press
        except: 
            continue                                          #If no key is pressed, continue the loop
   
   
#If the user presses the ESC key (ASCII value 27), exit the loop and program
        if ord(key) == 27:           #27 is the ASCII code for ESC
            break

#If the user presses backspace, remove the last typed character
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:      #Ensure there's text to delete
                current_text.pop()         #Remove the last character from current_text

        elif len(current_text) < len(target_text):
            current_text.append(key)       #Append what they type to the current text

                        
# Main function initializes the color pairs 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)



wrapper(main)