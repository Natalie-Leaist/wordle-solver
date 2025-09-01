class WordleBot:
    def __init__(self, game, solver, print_stuff = False):
        self.game = game
        self.solver = solver
        self.print_stuff = print_stuff

    def play(self):
        for i in range(self.game.max_attempts):
            guess = self.solver.choose_guess()
            if not guess:
                if self.print_stuff:
                    print("No candidates left!")
                break
            feedback = self.game.check_guess(guess)

            if self.print_stuff:
                print(f"Guess {i + 1}: {guess}, Feedback: {feedback}")
            if self.game.is_solved():
                if self.print_stuff:
                    print("Solved!")
                return (i + 1)
            self.solver.update_candidates(guess, feedback)

        if self.print_stuff:
            print("Failed to solve.")
        return (i + 1)