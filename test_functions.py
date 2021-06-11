""" Test for my functions.

    Note
    ----
    The Professor and I talked and she said it's ok to do only one function test due to the complexity of my code.
    But I did more anyways. :)
    
    The code I took to make my tests (with modifications)
    -----------------------------------------------------
        https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
"""

from choose_film import ChooseFilm
from read_script import ReadScript

class test_ChooseFilm():
    assert callable(ChooseFilm)
    var1 = ChooseFilm()
    assert isinstance(var1.movie_script, str)
    assert isinstance(var1.index, int)
    
    def test_choose_movie():
        assert callable(var1.choose_movie())
        assert isinstance(var1.choose_movie(), str)
        # can't test actual input unless I do a mock because I use random

def TestReadScript():
    assert callable(ReadScript)

# Testing user input
from unittest import mock
from unittest import TestCase
import game_functions
from choose_film import ChooseFilm


class Test(TestCase):
    # Testing get_level
    def test_get_level():
        assert callable(game_functions.get_level())
        
    def test_print_dialogue():
        assert callable(game_functions.print_dialogue())
        
    @mock.patch('game_functions.input', create=True)
    def test_get_level(self, mocked_input):
        mocked_input.side_effect = ['1']
        self.assertEqual(game_functions.get_level(), '1')
        
        mocked_input.side_effect = ['2']
        self.assertEqual(game_functions.get_level(), '2')
        
        mocked_input.side_effect = ['hello', '3']
        self.assertEqual(game_functions.get_level(), '3')
        
        mocked_input.side_effect = ['5', 'hello', '?', '2']
        self.assertEqual(game_functions.get_level(), '2')
        
     # Testing print_dialogue 
    @mock.patch('game_functions.input', create=True)
    def test_print_dialogue(self, mocked_input):
        mocked_input.side_effect = ['quit']
        self.assertEqual(game_functions.print_dialogue('4'), 'quit')
        
        mocked_input.side_effect = ['Avengers']
        self.assertEqual(game_functions.print_dialogue('1'), 'Avengers')
    
    # Testing guess_movie
    @mock.patch('game_functions.input', create=True)
    @mock.patch('choose_film.title', create=True)
    def test_guess_movie(self, mocked_input, mocked_title):
        mocked_input.side_effect = ['']
        mocked_title = ['Ant-Man']
        self.assertEqual(game_functions.guess_movie('QUIT'), False)
    
    
# the tests below are scrapped ideas that I wanted to implement but wasn't sure how to. Will eventually come back to these.
'''
def TestReadScript():
    assert callable(ReadScript)
        
def test_read_lines():
    var = ReadScript(1)
    assert callable(var.read_lines())
    assert isinstance(var.read_lines(), int) # assert when enters a number, returns number NEED HELP
    #assert isinstance(read_lines(), input) # assert when enters a string, returns input NEED HELP

class test_ChooseFilm():
    assert callable(ChooseFilm())
    #assert isinstance(title, str)
    #assert isinstance(movie_script, str)
    #assert isinstance(index, int)

def test_choose_movie():
    variable = ChooseFilm()
    assert callable(variable.choose_movie())
    assert isinstance(variable.choose_movie(), str)
    
def test_print_dialogue():
    assert callable(game_functions.print_dialogue())
    #assert isinstance(print_dialogue('string'), input) # if put in string, returns input
    assert isinstance(game_functions.print_dialogue(1), str)
    
def test_guess_movie():
    assert callable(game_functions.guess_movie('hello'))
    assert isinstance(game_functions.guess_movie('QUIT'), bool)
                                                   
    
def test_guess_incorrect():
    assert callable(game_functions.guess_incorrect('Ant-Man'))
    assert isinstance(game_functions.guess_incorrect('Ant-Man'), bool) # idk if this will work
    
'''
