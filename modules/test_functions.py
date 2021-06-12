""" Test for my functions.

    Note
    ----
    Professor Ellis and I talked and she said it's ok to do only one function test due 
    to the complexity of my code. But I did more anyways. :)
    
    The code I took to make my tests (with modifications)
    -----------------------------------------------------
        https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
        
    I worked with a student named Tony on developing his mock test, first by explaining the 
    code from the stack overflow link, above and then by going step by step with him to make 
    sure he could recreate it in his own test file. Our code will look similar because of this.
    
    Also: Because of the way I have my other files importing other files (modules.filename) pytest
    by itself won't run. You have to run !python -m pytest test_functions.py or !python -m pytest.
"""

from choose_film import ChooseFilm
from read_script import ReadScript

class test_ChooseFilm():
    assert callable(ChooseFilm)
    var1 = ChooseFilm()
    assert isinstance(var1.title, str)
    assert isinstance(var1.movie_script, str)
    assert isinstance(var1.index, int)
    
    def test_choose_movie():
        assert callable(var1.choose_movie())
        assert isinstance(var1.choose_movie(), str)
        # can't test actual input unless I do a mock because I use random

def TestReadScript():
    assert callable(ReadScript)

def test_guess_incorrect():
    assert callable(game_functions.guess_incorrect)

# Testing user input
from unittest import mock
from unittest import TestCase
import game_functions
from choose_film import ChooseFilm

# Class that holds my tests that use mock 
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
        mocked_input.side_effect = ['QUIT']
        mocked_title = ['Ant-Man']
        self.assertEqual(game_functions.guess_movie('QUIT'), False)
        self.assertEqual(game_functions.guess_movie('PLAY AGAIN'), True)
    
    
""" These are all the tests I wanted to do, but could not implement.""" 
     
#def test_read_lines():
#    var = ReadScript(1)
#    assert callable(var.read_lines())
#    assert isinstance(var.read_lines(), int) # assert when enters a number, returns number NEED HELP
#    assert isinstance(read_lines(), input) # assert when enters a string, returns input NEED HELP
    
#def test_guess_movie():
#    assert callable(game_functions.guess_movie('hello'))
#    assert isinstance(game_functions.guess_movie('QUIT'), bool)                                              
    
#def test_guess_incorrect():
#    assert isinstance(game_functions.guess_incorrect('Ant-Man'), bool)
    
    