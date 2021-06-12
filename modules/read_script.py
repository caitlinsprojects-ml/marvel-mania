import csv
import random
import script_variables as scripts
from choose_film import ChooseFilm  # access choose_movie function and its variables

class ReadScript():
    """ Class uses level and the ChooseFilm class to read the correct number of lines from random script. """
    
    def __init__(self, level):
        self.level = level
        self.movie_script = ''
        
    def read_lines(self):
        """ Reads specified number of lines from chosen movie script based on level.
        
        The variables below are the URLs of the code I used from outside sources (too long to comment):
            stack1:
                https://stackoverflow.com/questions/56436024/python-3-count-number-of-rows-in-a-csv
            programiz: 
                https://www.programiz.com/python-programming/reading-csv-files
            stack2:
                https://stackoverflow.com/questions/5832856/how-to-read-file-n-lines-at-a-time-in-python
        
        Parameters
        ----------
        None
        
        Returns
        -------
        level : integer
            Level is the level indicated by the user.
        """
        
        choose_var = ChooseFilm()
        self.movie_script = choose_var.choose_movie() # access randomly chosen movie 
        
        if self.level in [1, 2, 3, 4]:
            with open(self.movie_script, 'r') as film_dialogue:     # opens csv file and reads it
                var_file_num_lines = film_dialogue.readlines()      # stack1
                num_lines = len(var_file_num_lines) # total number of lines in file (bounds)
            
        # Prints amount of lines based on level 
            if self.level == 1:
                start = random.randrange(0, num_lines-15)
                
                # read 15 lines
                with open(self.movie_script, 'r') as film_dialogue: # programiz
                    for count, line in enumerate(film_dialogue):    # stack2
                        if count >= start and count < start + 16:
                            print(line)
                            
                return self.level
            
            elif self.level == 2:
                start = random.randrange(0, num_lines-9)
                
                # read 9 lines 
                with open(self.movie_script, 'r') as film_dialogue: # programiz
                    for count, line in enumerate(film_dialogue):    # stack2
                        if count >= start and count < start + 9:
                            print(line)
                            
                return self.level
            
            elif self.level == 3:
                start = random.randrange(0, num_lines-5)
                
                # read 5 lines
                with open(self.movie_script, 'r') as film_dialogue: # programiz
                    for count, line in enumerate(film_dialogue):    # stack2
                        if count >= start and count < start + 5:
                            print(line)
                            
                return self.level
            
            elif self.level == 4:
                start = random.randrange(0, num_lines-2)
                
                # read 2 lines
                with open(self.movie_script, 'r') as film_dialogue: # programiz
                    for count, line in enumerate(film_dialogue):    # stack2
                        if count >= start and count < start + 2:
                            print(line)
                            
                return self.level
                
        else:
            for level_number, level in zip([1, 2, 3, 4], ['Easy', 'Medium', 'Hard', 'Impossible']):
                print(level_number, level)
                
            return input('Please indicate the difficulty level by entering an integer between 1 and 4: \t')  
    