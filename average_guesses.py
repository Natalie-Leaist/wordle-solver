from word_list import WordList
from wordle_game import WordleGame
from wordle_solver import WordleSolver
from strategy import PartitionStrategy
from wordle_bot import WordleBot

words = WordList() #get list of words
solutions = WordList(filepath ="secret_words.txt").get_words() #can be replaced with a file of your choosing

max_guesses = 0
sum_guesses = 0

for s in solutions:
    game = WordleGame(s)
    solver = WordleSolver(words.get_words(), PartitionStrategy())
    bot = WordleBot(game, solver)
    n = bot.play()
    if n >= 7:
        print(f"The word {s} took {n} guesses :(")
    if n > max_guesses:
        max_guesses = n
    sum_guesses += n

avg_guesses = sum_guesses / len(solutions)

print("Average number of guesses:", avg_guesses)
print("Max guesses:", max_guesses)