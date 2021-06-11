import csv
import random
import script_variables as scripts

class ChooseFilm():
    """ Class to represent the current round's film.
    
    Attributes
    ----------
    movie_script : string
        String that contains the variable that contains the script csv file string from the scripts module.
    index : integer
        Integer that is the index of the title in the title list.
    title : string 
        Global attribute, holds title of random script.
     
    Methods
    -------
    choose_movie()
        Chooses a random title and returns the accompanying script in the movie_script attribute.
    """
    
    title = ''
    
    def __init__(self, movie_script = '', index = 0):
        """ Constructs the attributes for the ChooseFilms object.
        
        Parameters
        ----------
            movie_script : string
                String containing the script csv file, default is empty string.
            index : integer
                Index of the title in the title list, default is 0.
        """
        
        self.movie_script = movie_script
        self.index = index
        
    def choose_movie(self):
        """ Chooses a random movie and returns the script's csv.
        Parameters
        ----------
        None
                
        Returns
        -------
        movie_script : string
            String is the script csv file for the current round's movie.
        
        """
        # get title
        global title
        title = random.choice(scripts.title_list)
        
        # get index from list and match to csv file variable in script module
        self.index = scripts.title_list.index(title)
        
        # get variable that contains string path to script csv
        self.movie_script = scripts.movie_list[self.index]
        
        return self.movie_script

    
#class test_ChooseFilm():
#    assert callable(ChooseFilm)
#    assert isinstance(title, str)
#    assert isinstance(index, int)
#    assert isinstance(movie_script, str)