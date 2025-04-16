# yatzy.py
import random
from collections import Counter

class Yatzy:
    def __init__(self):
        self.dice = [0] * 5
        self.locked = [False] * 5
        self.roll()

    def roll(self):
        # """Roll all unlocked dice"""
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def lock(self, index):
        # """Lock a specific die (0-4)"""
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock(self, index):
        # """Unlock a specific die (0-4)"""
        if 0 <= index < 5:
            self.locked[index] = False

    def unlock_all(self):
        # """Unlock all dice"""
        self.locked = [False] * 5

    # Scoring methods
    def get_dice(self):
        return self.dice

    def _count(self):
        return Counter(self.dice)

    def Ones(self):
        return self.dice.count(1) * 1

    def Twos(self):
        return self.dice.count(2) * 2

    def Threes(self):
        return self.dice.count(3) * 3

    def Fours(self):
        return self.dice.count(4) * 4

    def Fives(self):
        return self.dice.count(5) * 5

    def Sixes(self):
        return self.dice.count(6) * 6

    def OnePair(self):
        counts = self._count()
        for num in sorted(counts, reverse=True):
            if counts[num] >= 2:
                return num * 2
        return 0

    def TwoPairs(self):
        counts = self._count()
        pairs = [num for num in counts if counts[num] >= 2]
        if len(pairs) >= 2:
            return sum(sorted(pairs, reverse=True)[:2]) * 2
        return 0

    def ThreeAlike(self):
        counts = self._count()
        for num in sorted(counts, reverse=True):
            if counts[num] >= 3:
                return num * 3
        return 0

    def FourAlike(self):
        counts = self._count()
        for num in sorted(counts, reverse=True):
            if counts[num] >= 4:
                return num * 4
        return 0

    def Small(self):
        return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0

    def Large(self):
        return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def FullHourse(self):
        counts = self._count()
        values = sorted(counts.values())
        if values == [2, 3]:
            return sum(self.dice)
        return 0

    def Chance(self):
        return sum(self.dice)

    def Yatzy(self):
        return 50 if len(set(self.dice)) == 1 else 0
