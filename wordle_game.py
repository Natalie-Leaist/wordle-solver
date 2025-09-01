from collections import Counter

class WordleGame:
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.max_attempts = 100   # extended for testing
        self.attempts = []

    def check_guess(self, guess):
        feedback = ["X"] * len(guess)
        secret_counter = Counter(self.secret_word)

        for i, letter in enumerate(guess):
            if letter == self.secret_word[i]:
                feedback[i] = "G"
                secret_counter[letter] -= 1

        for i, letter in enumerate(guess):
            if feedback[i] == "X" and secret_counter[letter] > 0:
                feedback[i] = "Y"
                secret_counter[letter] -= 1

        self.attempts.append((guess, feedback))
        return feedback

    def is_solved(self):
        return any(all(f == "G" for f in fb) for _, fb in self.attempts)
