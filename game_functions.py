import csv
import script_variables as scripts
from read_script import ReadScript
import choose_film as choose_film

def get_level():
    """ Introduction and gets level input.
    
    Parameters
    ----------
    None
     
    Returns
    -------
    level_input : string
        Returns the player's input level, either '1', '2', '3', or '4', as a string.
    """
    
    print('Levels:')
    for level_number, level in zip([1, 2, 3, 4], ['Easy', 'Medium', 'Hard', 'Impossible']):
                print(level_number, level)
            
    level_input = input('\n Welcome MCU Fans! To play, please enter a level (1, 2, 3, 4):\t')
    print('\n')
    
    while level_input not in ['1', '2', '3', '4']:
        for level_number, level in zip([1, 2, 3, 4], ['Easy', 'Medium', 'Hard', 'Impossible']):
                print(level_number, level)
        level_input = input('Please indicate the difficulty level ' +
                            'by entering an integer between 1 and 4: \t')
    
    print('\n')
    
    return level_input

def print_dialogue(level_input):
    """ Prints lines based on level and gets player's guess.
    
    Parameters
    ----------
    level_input : string
        The player's input level, either '1', '2', '3', or '4'.
    
    Returns
    -------
    guess : string
        The player's movie title guess.
    """
    
    level_input = int(level_input)
    var_to_read = ReadScript(level_input)
    var_to_read.read_lines()
    
    guess = input('Guess the movie title!: ')
    
    return guess

def guess_movie(guess):
    """ Takes guess and checks correctness. Then either calls guess_incorrect function 
        or prompts to play again or quit the game.
    
    Parameters
    ----------
    guess : string
        String contains player's movie title guess.
    
    Returns
    -------
    True : bool
        Returned if player would like to play again.
    
    False: bool
        Returned if player would like to quit the game entirely.
    
    guess_incorrect : bool
        Called guess_incorrect function if guess is incorrect. Function returns a boolean.
        guess_incorrect() returns True to play again or False to quit game entirely.
    """
    
    title = choose_film.title
    
    # Check for guess_incorrect()'s return 'QUIT'
    if guess == 'QUIT':
        
        return False
    
    # Check for guess_incorrect()'s return 'PLAY AGAIN' 
    elif guess == 'PLAY AGAIN':
        
        return True
    
    # Check correctness
    elif guess.lower() == title.lower():
        correct = input('Correct! Wow you really know your stuff. Would ' +
                        'you like to play again? Type yes/no: \t')
        
        if correct.lower() == 'yes':

            return True
            
        else:
            
            return False

    else:
        return guess_incorrect(title)
        
def guess_incorrect(title_name):
    """ When guess is incorrect, gets title list, quits the round, or allows player 
        to guess again depending on player input.
    
    Parameters
    ----------
    title_name : string
        The current round's movie title.
    
    Returns
    -------
    guess_movie(argument) : bool
        The result of calling function guess_movie() with a new guess (type string), 'PLAY AGAIN', 
        or 'QUIT' as the argument, depending on player input.
    """
    
    title = title_name
    
    # Inital prompt when guess is incorrect
    incorrect = input('Incorrect! Make sure to check your spelling, '+ 
                      'punctuation, and spacing. Titles are not case ' +
                      'sensitive.\n If you would like a list of acceptable ' +
                      'entries, type "films". Type "quit" to quit.\n Otherwise,' +
                      ' press any key to guess again.\n')
    
    # Get list of films
    if incorrect == 'films':
        print('\n')
        print(scripts.title_list)
        print('\n')
        
        new_guess = input('Guess again!: ')
        
        return guess_movie(new_guess)
    
    # To end this round
    elif incorrect.lower() == 'quit':
        quit = input('The correct film was ' + title + 
                     '. Want to play again? Enter yes/no: \t')

        if quit.lower() == 'yes':
            
            return guess_movie('PLAY AGAIN')
        
        else:

            return guess_movie('QUIT')
        
    # To simply guess again
    else:
        print('\n')
        new_guess = input('Guess again!: ')
        
        return guess_movie(new_guess)
    
