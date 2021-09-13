import pytest

import KMCmodel.size3D

test_size3D = KMCmodel.size3D.Size3D(1,2,3)

def test_size3D_creation_and_getters():
    assert test_size3D.width == 1
    assert test_size3D.height == 2
    assert test_size3D.depth == 3
    assert test_size3D.volume_size == 6

def test_size3D_setters_and_volume_size_calculation():
    test_size3D.width = 2
    assert test_size3D.width == 2
    assert test_size3D.volume_size == 12
    test_size3D.height = 3
    assert test_size3D.height == 3
    assert test_size3D.volume_size == 18
    test_size3D.depth = 4
    assert test_size3D.depth == 4
    assert test_size3D.volume_size == 24