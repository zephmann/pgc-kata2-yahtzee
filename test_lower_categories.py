# :coding: utf-8

import pytest

from yahtzee_categories import (
    BaseCategory,
    MatchCategory,
    CountCategory,
    SequenceCategory,
)


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,2,3,4,5), 0),  # no match
        ((1,1,1,2,3), 8),  # match
        ((1,2,2,2,3), 10),  # match
        ((1,2,3,3,3), 12),  # match
        ((6,2,6,3,6), 23),  # match shuffled
    ]
)
def test_three_count(dice, score):
    cat = CountCategory(counts=[3])
    assert cat.score(dice) == score



@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,2,3,4,5), 0),  # no match
        ((1,1,1,1,1), 50),  # match
        ((2,2,2,2,2), 50),  # match with different number
    ]
)
def test_yahtzee(dice, score):
    cat = CountCategory(counts=[5], multiplier=0, base=50)
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,2,3,4,5), 0),  # no match
        ((1,1,1,4,5), 0),  # no match
        ((1,1,1,1,1), 0),  # no match
        ((1,1,2,2,2), 25),  # match 2-3
        ((3,3,3,4,4), 25),  # match 3-2
        ((5,6,5,6,6), 25),  # match shuffled
    ]
)
def test_full_house(dice, score):
    cat = CountCategory(counts=[3,2], multiplier=0, base=25)
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,1,1,1,1), 0),  # no straight
        ((1,2,3,4,4), 30),  # 1 2 3 4 
        ((2,2,3,4,5), 30),  # 2 3 4 5
        ((3,3,4,5,6), 30),  # 3 4 5 6
    ]
)
def test_small_straight(dice, score):
    cat = SequenceCategory(length=4, multiplier=0, base=30)
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,1,1,1,1), 0),  # no straight
        ((1,2,3,4,4), 0),  # small straight 
        ((1,2,3,4,5), 40),  # 2 3 4 5
        ((2,3,4,5,6), 40),  # 3 4 5 6
    ]
)
def test_large_straight(dice, score):
    cat = SequenceCategory(length=5, multiplier=0, base=40)
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,1,1,1,1), 5),
        ((1,2,3,4,4), 14),   
        ((1,2,3,4,5), 15),
        ((2,3,4,5,6), 20),
    ]
)
def test_chance(dice, score):
    cat = BaseCategory()
    assert cat.score(dice) == score
