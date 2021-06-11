# marvel-mania

Welcome to my first working Python game! A few things to note before we get started...

  1. I  am not affiliated with Marvel or Disney in any capacity and do not own any of the CSV files. I got them from Kaggle and cleaned them up.

  2. This game was made for educaitonal purposes only and is not making money in any way.

  3. This is for extra credit for my coding class. Hi Professor! :)



Now for the meat and potatoes.

- The script to run this game is in the folder game_script and the file is called lets_play.py.
- The functions, class, and files that the script runs are in a folder called modules.
- The Marvel movie script CSV files are in a folder called marvel_dialogue_dataset, which is inside the modules folder.
- I don't know if Jupyter notebook was being weird but after submitting my project and trying to run it again it wouldn't run.
- So, to the best of my knowledge this code should work. If it doesn't, I'll fix it.

## about-the-game
Each round the player will choose a level between 1 and 4, from easiest to hardest, and a number of lies from one of twenty-three Marvel movies will print out. As the levels get harder the number of lines printed will decrease. The player will then guess the movie title. If the player would like to quit the game, simply typing "QUIT" when prompted to guess will quit that round. To get a list of films, the player will make a guess and then type "films". There are an unlimited number of rounds allowed.

Future implementations of this game will include:
- a timer
- a complex scoring system indicating number of first try correctness, number of correct answers per game, and total rounds played
- a scoring system that saves previous scores and presents data on player's best and worst known films and other player statistics.

- To run the game, run this code:
          
          from game_script import lets_play as play 
          play.lets_play()

## testing 
!pytest should be sufficient to run my tests. Not all tests have been created as I am still a beginning programmer, but I'm trying my best. :)
