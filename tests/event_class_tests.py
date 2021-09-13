import pytest

import KMCmodel.event

test_event = KMCmodel.event.Event()

def test_probability_getter():
    assert test_event.probability == None

def test_probability_setter():
    test_event.probability = 1
    assert test_event.probability == 1