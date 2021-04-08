# :coding: utf-8

from abc import ABC, abstractmethod


class BaseCategory(ABC):

    def __init__(self, multiplier=1, base=0):
        self._multiplier = multiplier
        self._base = base


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


# class FullHouse(BaseCategory):
#     def _filter_dice(self, dice):
#         # TODO update logic to work with MatchCategory
#         # how to ensure that different numbers match different counts?
#         if (
#             len(set(dice)) == 2 and
#             dice[0] == dice[1] and 
#             dice[3] == dice[4]
#         ):
#             return dice

#     def _score(self, dice):
#         return 25


class Chance(BaseCategory):
    def _score(self, dice):
        return sum(dice)


class SmallStraight(BaseCategory):
    def _filter_dice(self, dice):
        for pattern in ((1,2,3,4), (2,3,4,5), (3,4,5,6)):
            if set(pattern).issubset(dice):
                return dice

    def _score(self, dice):
        return 30


# chance is 1*d + 0
# ones is 1*d + 0  (filtered)
# yahtzee is 0*d + 50 (if filtered)

# list of counts to match
# "filter": {"type": "match", "value": 1},
# "filter": {"type": "count", "value": 3},
# "filter": {"type": "sequence", "value": 4},


# search backwards through count numbers,
# somehow pop out number that matches
