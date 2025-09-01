from word_list import WordList
from wordle_solver import WordleSolver
from strategy import PartitionStrategy

def print_instructions():
    print("You will be given a guess into the wordle game.")
    print("You will then be prompted to tell the program the result of the guess.")
    print("You will enter a string of characters (eg. GBYBB).")
    print("If the colour of a letter is green, enter G.")
    print("If the colour of a letter is yellow, enter Y.")
    print("If the colour of a letter is grey, enter X.")
    print("Enter Q to quit.")

def valid_input(feedback):
    if feedback == "Q":
        return True
    elif len(feedback) != 5:
        return False
    else:
        return set(feedback).issubset(set("GYX"))


words = WordList()
solver = WordleSolver(words.get_words(), PartitionStrategy())

print_instructions()

for attempt in range(1, 7):
    guess = solver.choose_guess()
    if not guess:
        print("No candidates left!")
        break

    print(f"Guess {attempt}: {guess}")
    feedback = input("Enter feedback: ").strip().upper()

    # keep asking until valid
    while not valid_input(feedback):
        print("Invalid input, try again.")
        feedback = input("Enter feedback (Q or 5 letter string of G/Y/X): ")

    if feedback == "Q":
        print("Exiting.")
        break

    if feedback == "GGGGG":
        print(f"Solved in {attempt} attempts!")
        break

    # Update candidates for next round
    solver.update_candidates(guess, feedback)
