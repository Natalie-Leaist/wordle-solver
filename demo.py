from word_list import WordList
from wordle_game import WordleGame
from wordle_solver import WordleSolver
from strategy import PartitionStrategy
from wordle_bot import WordleBot

words = WordList() #get list of words
game = WordleGame("sport") #start a game with the chosen word as the solution
solver = WordleSolver(words.get_words(), PartitionStrategy()) #start the solver
bot = WordleBot(game, solver, print_stuff=True) #create the bot (the player of the game)
bot.play() #start the game