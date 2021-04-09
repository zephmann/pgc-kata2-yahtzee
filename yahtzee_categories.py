# :coding: utf-8

from abc import ABC


class BaseCategory(ABC):

    def __init__(self, num_sides=6, name="", multiplier=1, base=0):
        self._multiplier = multiplier
        self._base = base
        self._num_sides = num_sides
        
        self.name = name

    def score(self, dice):
        """Return a score for the category based on the input dice roll.

        :param dice: tuple of input dice values.
        :return: corresponding score for the dice roll.
        """
        dice = sorted(dice)

        dice = self._filter_dice(dice)

        return self._score(dice) if dice else 0

    def _filter_dice(self, dice):
        """Filter out any invalid dies from *dice*

        :param dice: tuple of raw input dice values, assumes input values 
            are sorted in increasing order.
        :return: a new list of only valid dice values.
        """
        return dice

    def _score(self, dice):
        """Calculate and return an integer score based on *dice*

        :param dice: a tuple of int dice values.
        :return: the calculated score
        """
        return self._multiplier * sum(dice) + self._base


class MatchCategory(BaseCategory):
    
    def __init__(self, number, *args, **kwargs):
        super(MatchCategory, self).__init__(*args, **kwargs)

        # TODO handle multiple match conditions?
        self._number = number

    def _filter_dice(self, dice):
        return tuple(
            die for die in dice
            if die == self._number
        )



class CountCategory(BaseCategory):
    def __init__(self, counts, *args, **kwargs):
        super(CountCategory, self).__init__(*args, **kwargs)

        self._counts = sorted(counts, reverse=True)

    def _filter_dice(self, dice):
        unique_dice = set(dice)
        
        for count in self._counts:
            for die in unique_dice:
                if dice.count(die) >= count:
                    unique_dice.remove(die)
                    break
            else:
                return

        return dice


class SequenceCategory(BaseCategory):

    def __init__(self, length, num_sides=6, *args, **kwargs):
        super(SequenceCategory, self).__init__(*args, **kwargs)

        self._sequences = []

        end = num_sides + 1
        all_sides = range(1, end)

        for start, stop in enumerate(range(length, end), 1):
            self._sequences.append(
                set(all_sides[start:stop])
            )

    def _filter_dice(self, dice):
        for pattern in self._sequences:
            if pattern.issubset(dice):
                return dice
