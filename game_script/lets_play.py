import sys
sys.path.append('/home/c3connol/Project_Sp21/modules/')

import game_functions as game, read_script, choose_film, script_variables

def lets_play():
    """ Main play game function.
    
    Note
    ----
    I heavily modified the script from the A3 chatbot.
    
    I also helped a student named Angela understand the chatbot code and why returns are important for functions.
    
    Another small note: I helped a few students debug their code (figure out error messages and why) so I should be 
    credited in their project with what I helped them with.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    '*snap*' : string
        Returns a Thanos snap if player wants to quit the game entirely.
    restart() : function
        Returns if player wants to play again.
    """
    
    play = True 
    
    while play:
        # Introduces and gets level
        level = game.get_level() 
        
        # Uses level to print dialogue and gets guess 
        guess = game.print_dialogue(level)
        
        # Checks if guess is correct and gets play status (continue playing or not)
        play_status = game.guess_movie(guess)
        
        # Decides whether to restart or end the game
        if play_status == True:
            break
        
        elif play_status == False:
            print('\n')
            print('Okie dokie! Avengers dis-assemble, I guess!')
            return '*snap*'
        
        # This should never print out. If it does, something has gone very wrong.
        else:
            print('\n')
            print("So, your code has failed spectacularly. You screwed up. " +
            "You know what you did was wrong. The question is, how are you going " + 
            "to make things right? (To restart the game, rerun play.lets_play())")
            return
        
    return restart()

def restart():
    """ Replay/continue playing function.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    restart : string
        Returns what lets_play() returns.
        Either calls restart() again or returns a Thanos snap.
    """
    
    restart = lets_play()
    
    return restart 
