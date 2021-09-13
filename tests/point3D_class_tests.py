import pytest

import KMCmodel.point3D

test_point3D = KMCmodel.point3D.Point3D(1,2,3)

def test_creating_point3d_and_getters():
    assert test_point3D.x == 1
    assert test_point3D.y == 2
    assert test_point3D.z == 3

def test_point3d_setters():
    test_point3D.x = 5
    test_point3D.y = 10
    test_point3D.z = 15
    assert test_point3D.x == 5
    assert test_point3D.y == 10
    assert test_point3D.z == 15