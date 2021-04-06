# :coding: utf-8

from abc import ABC, abstractmethod


class YahtzeeCategory(ABC):
    def __init__(self):
        pass

    def score(self, dice):
        """Return a score for the category based on the input dice roll.

        :param dice: tuple of input dice values.
        :return: corresponding score for the dice roll.
        """
        dice = sorted(dice)

        dice = self._filter_dice(dice)

        return self._score(dice)

    def _filter_dice(self, dice):
        """Filter out any invalid dies from *dice*

        :param dice: tuple of raw input dice values, assumes input values 
            are sorted in increasing order.
        :return: a new list of only valid dice values.
        """
        return dice

    @abstractmethod
    def _score(self, dice):
        """Calculate and return an integer score based on *dice*

        :param dice: a tuple of 5 int dice values.
        :return: the calculated score
        """


class UpperCategory(YahtzeeCategory):
    _number = 0

    def _filter_dice(self, dice):
        return tuple(
            die for die in dice
            if die == self._number
        )

    def _score(self, dice):
        return self._number * len(dice)


class Ones(UpperCategory):
    _number = 1


class Twos(UpperCategory):
    _number = 2


class Threes(UpperCategory):
    _number = 3


class Fours(UpperCategory):
    _number = 4


class Fives(UpperCategory):
    _number = 5


class Sixes(UpperCategory):
    _number = 6
