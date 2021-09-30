import KMCmodel.space
import KMCmodel.size3D
import KMCmodel.cell
import KMCmodel.diffusion
import KMCmodel.color
import numpy as np

def test_space_creation_and_size_getter():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.size.width == 5
    assert test_space.size.height == 5
    assert test_space.size.depth == 5

def test_space_cells_getter():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert isinstance(test_space.cells, np.ndarray) == True
    assert isinstance(test_space.cells[0, 0, 0], KMCmodel.cell.Cell) == True
    assert test_space.cells[0, 0, 0] == KMCmodel.cell.Cell(0, 0, 0)

def test_space_allDiffusions_getter():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert isinstance(test_space.allDiffusions, np.ndarray) == True
    assert test_space.allDiffusions.shape == (5, 5, 5, 17)
    assert isinstance(test_space.allDiffusions[0, 0, 0, 0], KMCmodel.diffusion.Diffusion)

def test_space_possibleDiffusions_getter():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.possibleDiffusions == []

def test_space_possibleDiffusions_setter():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.possibleDiffusions == []

    origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    test_diffusion = KMCmodel.diffusion.Diffusion(origin_cell_test, target_cell_test)

    test_space.possibleDiffusions = test_diffusion
    assert len(test_space.possibleDiffusions) == 1
    assert test_space.possibleDiffusions[0] == test_diffusion

    second_origin_cell_test = KMCmodel.cell.Cell(2, 2, 2)
    second_target_cell_test = KMCmodel.cell.Cell(3, 3, 3)
    second_test_diffusion = KMCmodel.diffusion.Diffusion(second_origin_cell_test, second_target_cell_test)

    test_space.possibleDiffusions = second_test_diffusion
    assert len(test_space.possibleDiffusions) == 2
    assert test_space.possibleDiffusions[1] == second_test_diffusion
    assert (test_space.possibleDiffusions[1] == test_diffusion) == False

def test_space_cumulated_probability():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.cumulated_probability == 0

def test_space_getTransparentColor_and_getColorAtIndex():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.getColorAtIndex(0) == KMCmodel.color.Color(0, 0, 0, 0)

    test_space.getTransparentColor()

    assert test_space.getColorAtIndex(1) == KMCmodel.color.Color(0, 0, 0, 0)

def test_space_getIndexOfColor():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.getIndexOfColor(KMCmodel.color.Color(0, 0, 0, 0)) == 0

    test_space.getTransparentColor()

    assert test_space.getIndexOfColor(KMCmodel.color.Color(0, 0, 0, 0)) == 0

    test_space.getTransparentColor()

    assert test_space.getIndexOfColor(KMCmodel.color.Color(0, 0, 0, 0)) == 0

def test_space_getNewColor():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.getNewColor() == 1
    assert isinstance(test_space.getColorAtIndex(1), KMCmodel.color.Color) == True

    given_color = test_space.getColorAtIndex(1)
    assert test_space.getColorAtIndex(1) == given_color
    assert test_space.getIndexOfColor(given_color) == 1

def test_space_cells_getColor():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    assert test_space.cells_getColor(0, 0, 0) == KMCmodel.color.Color(0, 0, 0, 0)
    assert test_space.cells_getColor(1, 2, 3) == KMCmodel.color.Color(0, 0, 0, 0)

def test_space_cells_setColor():
    n = 5
    test_size = KMCmodel.size3D.Size3D(n, n, n)
    test_space = KMCmodel.space.Space(test_size)

    test_color = KMCmodel.color.Color(255, 0, 0, 1)
    test_space.cells_setColor(0, 0, 0, test_color)

    assert test_space.cells_getColor(0, 0, 0) == KMCmodel.color.Color(255, 0, 0, 1)

    second_test_color = KMCmodel.color.Color(255, 152, 3, 1)
    test_space.cells_setColor(3, 2, 1, second_test_color)
    assert test_space.cells_getColor(3, 2, 1) == KMCmodel.color.Color(255, 152, 3, 1)
