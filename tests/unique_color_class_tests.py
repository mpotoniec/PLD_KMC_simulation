import pytest
import numpy as np

import KMCmodel.uniqueColor
import KMCmodel.color

test_uniqueColor = KMCmodel.uniqueColor.UniqueColor()

def test_getNewColor_method():
    assert test_uniqueColor.getNewColor() == 1

def test_uniqueColor_method():
    assert test_uniqueColor.uniqueColor() == None

def test_getColorAtIndex_method():
    assert test_uniqueColor.getColorAtIndex(0)
    assert test_uniqueColor.getColorAtIndex(1)

def test_getIndexOfColor_method():
    R = np.ubyte(0)
    G = np.ubyte(0)
    B = np.ubyte(0)
    A = np.ubyte(0)
    test_color = KMCmodel.color.Color(R,G,B,A)
    assert test_uniqueColor.getIndexOfColor(test_color)