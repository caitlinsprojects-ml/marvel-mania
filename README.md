# marvel-mania

Welcome to my first working Python game! A few things to note before we get started...

  1. I  am not affiliated with Marvel or Disney in any capacity and do not own any of the CSV files. I got them from Kaggle and cleaned them up.

  2. This game was made for educational purposes only and is not making money in any way.

  3. This is for extra credit for my coding class. Hi Professor! :)



## about-code-setup
(Copied from the MarvelManiaProject.ipynb's project description)  
##### game_script/lets_play
- The file contains the main script to run my game, a function called lets_play. It also contains the function that restarts my game if the player wants to play another round.
##### modules/marvel_dialogue_dataset
- This folder contains the csv files for 23 Marvel movie scripts. I got them from Kaggle and reformatted them.
##### modules/game_functions
- This file contains most of my functions. It has functions get_input, print_dialogue, guess_movie and guess_incorrect.
##### modules/choose_film
- This file contains the ChooseMovie class which contains the function/method choose_movie.
##### modules/read_script*
- This file contains the ReadScript class which contains the function/method read_lines.
##### modules/script_variables
- This file contains all the csv variables for easy access and two lists: a list of string movie titles and a corresponding list of csv-containing variables.
##### modules/test_functions
- This file contains the tests for my functions. !pytest will run this file.
- To the best of my knowledge this code should work.

## how-to-play
Each round the player will choose a level between 1 and 4, from easiest to hardest, and a number of lines from one of twenty-three Marvel movies will print out. As the levels get harder the number of lines printed will decrease. The player will then guess the movie title. 

If the player would like to quit the game, simply typing "QUIT" when prompted to guess will quit that round. To get a list of films, the player will make a guess and then type "films". There are an unlimited number of rounds allowed.

## about-future-edits 

Future additions to this game will include:
- a timer
- a complex scoring system indicating number of first try correctness, number of correct answers per game, and total rounds played
- a scoring system that saves previous scores and presents data on player's best and worst known films and other player statistics.
- graphics
- sequels for Marvel Disney+ tv shows, Marvel Netflix shows, Agents of S.H.I.E.L.D. and Agent Carter

## run-game
- To run the game, either run the code in the ipynb file or run this code:
          
          from game_script import lets_play as play 
          play.lets_play()

## testing 
!pytest should be sufficient to run my tests. Not all tests have been created as I am still a beginning programmer.
