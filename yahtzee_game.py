# :coding: utf-8

import json

from yahtzee_categories import (
    BaseCategory,
    MatchCategory,
    CountCategory,
    SequenceCategory,
)

DEFAULT_NUM_SIDES = 6
DEFAULT_NUM_DICE = 5


def YahtzeeGame():
    category_types = {
        "base": BaseCategory,
        "match": MatchCategory,
        "count": CountCategory,
        "sequence": SequenceCategory,
    }

    def __init__(
        self, 
        num_sides=DEFAULT_NUM_SIDES, 
        num_dice=DEFAULT_NUM_DICE, 
        categories=None
    ):
        self._num_sides = num_sides
        self._num_dice = num_dice
        
        self._categories = categories or []
        
        self._scores = {
            category.name: None for category in self._categories
        }

    def load_from_config(self, config_file):
        """Load the game settings from a JSON configuration file."""
        with open(config_file, "r") as f:
            config_data = json.load(f)

        self._num_sides = config_data.get("num_sides", DEFAULT_NUM_SIDES)
        self._num_dice = config_data.get("num_dice", DEFAULT_NUM_DICE)

        self._categories = []
        for category in config_data.get("categories", []):
            category_type = category.pop("__type__")
            self.add_category(category_type, **category)

    def add_category(category_type, *args, **kwargs):
        # TODO 
        category_class = self.category_types.get(category_type)
        self._categories.append(category_class(*args, **kwargs))

    def reset_game(self):
        self._scores = {
            category.name: None for category in self._categories
        }

    def roll(self):
        """Generate roll and return calculated scores."""
        # generate random numbers

        # return list of scores

    def record_score(category_name, dice):
        """Record the roll in the selected category."""


# initialize score dictionary, combine with categories?
# function to start a turn
# user picks which category to use
# records score in category
# if no categories left then game over

