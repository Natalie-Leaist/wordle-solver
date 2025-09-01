from collections import Counter
from strategy import GuessStrategy

class WordleSolver:
    def __init__(self, wordlist, strategy: GuessStrategy):
        self.candidates = wordlist
        self.strategy = strategy

    def update_candidates(self, guess, feedback):
        new_candidates = []
        for word in self.candidates:
            if self._matches(word, guess, feedback):
                new_candidates.append(word)
        self.candidates = new_candidates

    def _matches(self, word, guess, feedback):
        word_counter = Counter(word)

        for i, (g, fb) in enumerate(zip(guess, feedback)):
            if fb == "G":
                if word[i] != g:
                    return False
                word_counter[g] -= 1

        for i, (g, fb) in enumerate(zip(guess, feedback)):
            if fb == "Y":
                if g == word[i]:
                    return False
                if word_counter[g] <= 0:
                    return False
                word_counter[g] -= 1
            elif fb == "X":
                if word_counter[g] > 0:
                    return False
        return True

    def choose_guess(self):
        return self.strategy.choose(self.candidates)