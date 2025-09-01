import math
from word_list import WordList
from collections import defaultdict, Counter

probe_list = WordList(filepath ='probes.txt').get_words()

# parent class for strategies
class GuessStrategy:
    def choose(self, candidates):
        raise NotImplementedError


class FirstStrategy(GuessStrategy):
    def choose(self, candidates):
        return candidates[0] if candidates else None


class RandomStrategy(GuessStrategy):
    def choose(self, candidates):
        import random
        return random.choice(candidates) if candidates else None


class FrequencyStrategy(GuessStrategy):
    def choose(self, candidates):
        if not candidates:
            return None
        freq = Counter("".join(candidates))
        def score(word): return sum(freq[c] for c in set(word))
        return max(candidates, key=score)

class PartitionStrategy(GuessStrategy):
    def __init__(self, first_guess="salet", restrict_to_candidates=True):
        self.first_guess = first_guess
        self.first_move_done = False
        self.restrict_to_candidates = restrict_to_candidates

    def choose(self, candidates, all_words=None):
        if not candidates:
            return None
        if not self.first_move_done:
            self.first_move_done = True
            return self.first_guess
        # Pick from all words if allowed
        search_space = candidates + probe_list

        best_guess = None
        best_score = math.inf
        for guess in search_space:
            score = expected_partition_size(guess, candidates)
            if score < best_score:
                best_score = score
                best_guess = guess
        return best_guess

def expected_partition_size(guess, candidates):
    """Expected size of remaining candidates if we guess this word."""
    partitions = defaultdict(list)

    for secret in candidates:
        fb = compute_feedback(guess, secret)
        partitions[fb].append(secret)

    total = len(candidates)
    expected = 0
    for group in partitions.values():
        size = len(group)
        expected += (size / total) * size
    return expected

def compute_feedback(guess, secret):
    feedback = ["X"] * len(guess)
    secret_counter = Counter(secret)

    for i, g in enumerate(guess):
        if secret[i] == g:
            feedback[i] = "G"
            secret_counter[g] -= 1

    for i, g in enumerate(guess):
        if feedback[i] == "B" and secret_counter[g] > 0:
            feedback[i] = "Y"
            secret_counter[g] -= 1

    return "".join(feedback)

