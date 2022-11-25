# -*- coding: utf-8 -*-
"""
Hangman - James Foulkes 
"""

###############################################################################
# IMPORTS
###############################################################################

# To clear screen every iteration 
from IPython.display import clear_output 

# To choose random word from word list
from random import choice 

###############################################################################
# FUNCTIONS
###############################################################################

# Graphics
def Print_Graphics(wrong_guesses):
  ''' Print the graphics for the game,
    based on the number of incorrect guesses''' 

  # List of possible body parts
  body_parts = ['  O     |', '  |     |',' /|     |',
                ' /|\    |', ' /      |', ' / \    |']
    
  # How many lines to print
  lines = 4 if wrong_guesses != 0 else 5

  # Check number provided is usable
  if 0 <= wrong_guesses <= 6:
    print('  +-----+')  # Print top of frame
    print('  |     |')
    
  # Print the correct body parts for current state
    if wrong_guesses > 0:
      if wrong_guesses > 1:
        print(body_parts[0])
        lines -= 1

      if wrong_guesses > 4:
        print(body_parts[3])
        lines -= 1

      print(body_parts[wrong_guesses-1])

    for i in range(lines):
      print('        |')  # Print the lines
        
    print('==========')  # Print the floor

###############################################################################

# Word Selection
def Get_Word(file_name):
  '''Gets random word from a file containing a list of words'''

  # Initialise word storage
  words = []

  # Go through file, add words to list
  with open(file_name) as file:
    for line in file:
      words.append(line.strip())
  
  # Return random word from list
  return choice(words)

###############################################################################

# Recieve and Validate User's Guess 
def Get_Guess(user_guesses):
  '''Receive, then validate, user's guess'''

  # Acceptable inputs
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
              "j", "k", "l", "m", "n", "o", "p", "q", "r", 
              "s", "t", "u", "v", "w", "x", "y", "z"]

  while True:
    print("") # For ease of reading output

    # Take guess
    guess = input("Guess: ").lower().strip() 
    # Use .lower() to accept capital letter input from user
    
    if guess in alphabet and guess not in user_guesses:
      # Input is new letter
      user_guesses.append(guess) # add to list of guesses
      break # Break loop
    
    elif guess in user_guesses:
      # Already guessed letter
      print("You've already guessed " + guess + ". Please try a different letter.")
      # Continue loop

    else:
      # Invalid
      print("Invalid input. Please try again.")
      # Continue loop
  
  # Return the user's new guess
  return guess 

###############################################################################

# Word Display (Replace Unknown Letters with Underscore)

def Print_Word(word, user_guesses):
  '''prints word, replaces unknown letters with underscores'''

  # Initialise word tracker
  printed_word = '' 

  # Go through letters in the word. 
  # Check if user guessed them
  for letter in word:
    if letter in user_guesses:
      # Guessed letter
      printed_word += letter + " " # letter will be printed

    else:
      # Letter not guessed
      printed_word += "_ " # letter will not be shown

  # Show user
  print("Word: " + printed_word) 

  # Return word for win check
  return printed_word

###############################################################################

# Print Guesses
def Print_Guesses(all_guesses):
  '''displays all guesses the user has currently made'''

  # Initialise guess display
  guesses = "Guesses: "

  # Add guesses to displa
  for letter in all_guesses:
    guesses += letter + ", "

  #Show user
  print(guesses)

###############################################################################

#Difficulty Selection
def Difficulty():
  '''allows player to select difficulty level 
  by returning value to assign wrong_count'''

  # Loop until suitible answer given
  while True:
    print("\nPlease enter a difficulty level (1-4):\n \n1) Normal \n2) Hard")
    print("3) Very Hard \n4) Impossible")
    print("\nOr type 'info' for more detail on each difficulty level. \n")
    level = input("Level: ").lower().strip()

    # Info
    if level == "info":
      clear_output()
      print("Normal: 6 wrong guesses, you lose.")
      print("Hard: 4 wrong guesses, you lose.")
      print("Very Hard: 2 wrong guesses, you lose.")
      print("Impossible: 1 wrong guess, you lose. \n")

      # Return user to difficulty options when ready 
      input("Press enter to return to selections. ")
      clear_output()
    
    # Normal, Hard and Very Hard
    elif level in ["1", "2", "3"]:
      # Formula for wrong_count value: f(x) = 2(x - 1)
      return (int(level)*2 - 2) 

    # Formula doesn't work for 'Impossible' (x = 4). 
    # So assign seperately.

    # Impossible
    elif level == "4":
      return 5 

    #Error
    else:
      clear_output()
      print("Error. Please try again.")

############################################################################### 

# Main Program (Gameplay)
def Main_Program():
  '''runs game'''

  # Initialise random word, letters list and wrong guess counter
  word = Get_Word("wordlist.txt")
  user_guesses = []
  wrong_count = Difficulty()
  clear_output()

  # Print initial state of game
  Print_Graphics(wrong_count) 
  Print_Word(word, user_guesses)

  # Loop until too many wrong guesses:
  while wrong_count < 6: 
    # Get users guess, validate it until accepted
    guess = Get_Guess(user_guesses)

    # Increment wrong guess counter if letter not in word
    if guess not in word:
      wrong_count += 1

    # Print out the state of the game 
    clear_output() # Clear old graphics

    Print_Graphics(wrong_count) 

    win_check = Print_Word(word, user_guesses) # Store output for win check

    Print_Guesses(user_guesses)

    # Win check
    if "_" not in win_check:
      # All letters found (Player has won)
      break # Exit game loop
  
  # Print result
  if wrong_count < 6:
    # Player found all letters
    print("\nYOU WIN!")

    # Acknowledge a perfect game
    if wrong_count == 0:
      print("\nWow! \nYou played a perfect game! \nCONGRATULATIONS!")

  else:
    # Six wrong guesses
    print("\nYou lose.")

  #Tell user the correct answer
  print("\nThe full word was " + word + ".")

###################################################################################

# Game Loop
def Game_Loop():
  '''Allows user to keep playing until otherwise specified'''

  # Greet user
  print("WELCOME!")

  # Loop Game until player decides not to replay
  while True:
    Main_Program() # Run game

    # Ask user if they want anther round 
    replay = input("\nPlay again? (yes/no): ").lower().strip()
   
    # Keep asking until a yes/no answer given
    while replay not in ["yes", "no"]:
      clear_output()
      replay = input("Error. \nPlay Again? (yes/no): ").lower().strip()

   # End game when player says "no"
    if replay == "no":
      print("\nThanks For Playing!")
      break

###############################################################################
# Start Program
###############################################################################

# Call Game Loop Function to start
Game_Loop()

###############################################################################
# Thanks for the fun course!
# Really enjoyed it and learned a lot.
# Cheers,
# JF. :)
###############################################################################

