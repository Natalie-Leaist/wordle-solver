A fun Python project that can play and solve Wordle puzzles!

### Scripts:
- demo.py: example script to run the solver with the solution word of your choosing
- interactive_solver.py: the solver acts as a helper while the user plays wordle, recommending guesses and asking the human for feedback after each guess
- average_guesses.py: runs the game many times in a row with different solution words (found in the file secret_words.txt), and finds the average and maximum number of guesses across all the test games

### Project Files:
wordle_game.py: defines the WordleGame class
- Stores the solution word and max number of guesses
- Provides feedback for each guess:
  - G = Green (correct letter, correct spot)  
  - Y = Yellow (correct letter, wrong spot)  
  - X = Grey (letter not in word)
- checks if the solution word has been guessed

wordle_solver.py: defines the WordleSolver class
- maintains and updates the list of solution candidates

strategy.py: defines several different guessing strategies
- FirstStrategy: selects the first word from the list of possible candidates
- RandomStrategy: picks a random word from the candidate list
- FrequencyStrategy: scores words by letter frequency across all candidates and chooses the one with the most common letters
- PartitionStrategy: plays a strong opener ('salet'), then chooses the guess that minimizes the expected size of the remaining candidate list, maximizing information gain

wordle_bot.py: defines the WordleBot class
- automatically plays a game of wordle using the WordleGame class and WordleSolver class

word_list.py: defines the WordList class
- loads words from a file and stores them as a list

### Credits
- Word list (`words.txt`) adapted from several commonly available Wordle word lists published online
- Inspired by the original Wordle game created by Josh Wardle





