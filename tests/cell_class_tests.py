import pytest
import numpy as np

import KMCmodel.cell
import KMCmodel.color

def test_cell_x_getter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    assert test_cell.x == 1

def test_cell_x_setter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    test_cell.x = 5
    assert test_cell.x == 5

def test_cell_y_getter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    assert test_cell.y == 2

def test_cell_y_setter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    test_cell.y = 5
    assert test_cell.y == 5

def test_cell_z_getter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    assert test_cell.z == 3

def test_cell_z_setter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    test_cell.z = 5
    assert test_cell.z == 5

def test_cell_energy_getter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    assert test_cell.energy == 0

def test_cell_energy_setter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    test_cell.energy = 1.2
    assert test_cell.energy == 1.2

def test_cell_equality():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    assert test_cell == KMCmodel.cell.Cell(1, 2, 3)

def test_cell_neighbourhood_getter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    assert isinstance(test_cell.neighbourhood, np.ndarray)

def test_cell_neighbourhood_setter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)

    test_cell.neighbourhood[0] = KMCmodel.cell.Cell(0,0,0)
    test_cell.neighbourhood[10] = KMCmodel.cell.Cell(10,10,10)
    test_cell.neighbourhood[25] = KMCmodel.cell.Cell(25,25,25)

    assert test_cell.neighbourhood[1] == None
    assert test_cell.neighbourhood[0] == KMCmodel.cell.Cell(0,0,0)
    assert test_cell.neighbourhood[10] == KMCmodel.cell.Cell(10,10,10)
    assert test_cell.neighbourhood[25] == KMCmodel.cell.Cell(25,25,25)

def test_cell_color_getter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)
    assert test_cell.color == KMCmodel.color.Color(0, 0, 0, 0)

def test_cell_color_setter():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)

    for i in range(26):
        test_cell.neighbourhood[i] = KMCmodel.cell.Cell(i , 0, 0)

    test_cell.color = KMCmodel.color.Color(255, 0, 0, 1)
    assert test_cell.color == KMCmodel.color.Color(255, 0, 0, 1)

def test_getMostPopularColorInNeighbourhood():
    test_cell = KMCmodel.cell.Cell(1, 2, 3)

    for i in range(26):
        test_cell.neighbourhood[i] = KMCmodel.cell.Cell(i, 0, 0)
        for j in range(26):
            test_cell.neighbourhood[i].neighbourhood[j] = KMCmodel.cell.Cell(i, j, 0)

    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(0,0,0,0)

    test_cell.neighbourhood[0].color = KMCmodel.color.Color(255, 0, 0, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 0 ,0, 1)

    test_cell.neighbourhood[1].color = KMCmodel.color.Color(255, 155, 0, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 0 ,0, 1)

    test_cell.neighbourhood[2].color = KMCmodel.color.Color(255, 0, 0, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 0 ,0, 1)

    test_cell.neighbourhood[3].color = KMCmodel.color.Color(255, 155, 0, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 0 ,0, 1)

    test_cell.neighbourhood[4].color = KMCmodel.color.Color(255, 155, 0, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 155 ,0, 1)

    test_cell.neighbourhood[5].color = KMCmodel.color.Color(255, 155, 25, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 155 ,0, 1)

    test_cell.neighbourhood[6].color = KMCmodel.color.Color(255, 155, 25, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 155 ,0, 1)

    test_cell.neighbourhood[7].color = KMCmodel.color.Color(255, 155, 25, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 155 ,0, 1)

    test_cell.neighbourhood[8].color = KMCmodel.color.Color(255, 155, 25, 1)
    assert test_cell.getMostPopularColorInNeighbourhood() == KMCmodel.color.Color(255, 155 ,25, 1)
