import pytest
import numpy as np

import KMCmodel.color

R = np.ubyte(0)
G = np.ubyte(-1)
B = np.ubyte(-1)
A = np.ubyte(-1)

RGB = np.array([-1,0,0],dtype=np.ubyte)

test_color = KMCmodel.color.Color(R,G,B,A)

def test_color_creation_and_getters():
    test_color = KMCmodel.color.Color(R,G,B,A)
    assert test_color.R == R
    assert test_color.G == G
    assert test_color.B == B
    assert test_color.A == A

def test_color_setters():
    test_color.R = 120
    test_color.G = 240
    test_color.B = 15
    test_color.A = 0
    assert test_color.R == 120
    assert test_color.G == 240
    assert test_color.B == 15
    assert test_color.A == 0

def test_equality():
    c1 = KMCmodel.color.Color(R,G,B,A)
    c2 = KMCmodel.color.Color(R,G,B,A)
    assert c1 == c1
    assert c1 == c2
    #c2.R = np.ubyte(-1)
    #assert c1 == c2