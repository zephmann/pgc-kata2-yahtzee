# :coding: utf-8

import pytest

import yahtzee


@pytest.mark.parametrize(
    "dice, score",
    [
        ((2,3,4,5,6), 0),  # no ones
        ((1,2,3,4,5), 1),  # one ones
        ((1,1,3,4,5), 2),  # two ones
        ((1,1,1,4,5), 3),  # three ones
        ((1,1,1,1,5), 4),  # four ones
        ((1,1,1,1,1), 5),  # five ones
        ((5,4,3,2,1), 1),  # one ones, reversed
    ]
)
def test_ones(dice, score):
    cat = yahtzee.Ones()
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,3,4,5,6), 0),  # no twos
        ((1,2,3,4,5), 2),  # one twos
        ((1,2,2,4,5), 4),  # two twos
        ((1,2,2,2,5), 6),  # three twos
        ((1,2,2,2,2), 8),  # four twos
        ((2,2,2,2,2), 10),  # five twos
        ((5,4,3,2,1), 2),  # one twos, reversed
    ]
)
def test_twos(dice, score):
    cat = yahtzee.Twos()
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,2,4,5,6), 0),  # no threes
        ((1,2,3,4,5), 3),  # one threes
        ((1,2,3,3,5), 6),  # two threes
        ((1,2,3,3,3), 9),  # three threes
        ((3,2,3,3,3), 12),  # four threes
        ((3,3,3,3,3), 15),  # five threes
        ((5,4,3,2,1), 3),  # one threes, reversed
    ]
)
def test_threes(dice, score):
    cat = yahtzee.Threes()
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,2,3,5,6), 0),  # no fours
        ((1,2,3,4,5), 4),  # one fours
        ((1,2,3,4,4), 8),  # two fours
        ((4,2,3,4,4), 12),  # three fours
        ((4,4,3,4,4), 16),  # four fours
        ((4,4,4,4,4), 20),  # five fours
        ((5,4,3,2,1), 4),  # one fours, reversed
    ]
)
def test_fours(dice, score):
    cat = yahtzee.Fours()
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,2,3,4,6), 0),  # no fives
        ((1,2,3,4,5), 5),  # one fives
        ((5,2,3,4,5), 10),  # two fives
        ((5,5,3,4,5), 15),  # three fives
        ((5,5,5,4,5), 20),  # four fives
        ((5,5,5,5,5), 25),  # five fives
        ((5,4,3,2,1), 5),  # one fives, reversed
    ]
)
def test_fives(dice, score):
    cat = yahtzee.Fives()
    assert cat.score(dice) == score


@pytest.mark.parametrize(
    "dice, score",
    [
        ((1,2,3,4,5), 0),  # no sixes
        ((1,2,3,4,6), 6),  # one sixes
        ((6,2,3,4,6), 12),  # two sixes
        ((6,6,3,4,6), 18),  # three sixes
        ((6,6,6,4,6), 24),  # four sixes
        ((6,6,6,6,6), 30),  # five sixes
        ((6,4,3,2,1), 6),  # one sixes, reversed
    ]
)
def test_sixes(dice, score):
    cat = yahtzee.Sixes()
    assert cat.score(dice) == score


