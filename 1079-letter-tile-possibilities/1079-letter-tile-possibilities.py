from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        self.ans = 0
        freq = Counter(tiles)

        def backtrack():
            for ch in freq:
                if freq[ch] == 0:
                    continue

                self.ans += 1      # Count current sequence

                freq[ch] -= 1      # Choose
                backtrack()        # Explore
                freq[ch] += 1      # Undo

        backtrack()
        return self.ans