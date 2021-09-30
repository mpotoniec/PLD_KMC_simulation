import KMCmodel.diffusion
import KMCmodel.cell
import KMCmodel.adsorption
import KMCmodel.color


def test_diffusion_creation_and_cells_getter():
    origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    test_diffusion = KMCmodel.diffusion.Diffusion(origin_cell_test, target_cell_test)

    assert test_diffusion.originCell == origin_cell_test
    assert test_diffusion.targetCell == target_cell_test

def test_diffusion_cells_setter():
    origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    test_diffusion = KMCmodel.diffusion.Diffusion(origin_cell_test, target_cell_test)

    assert test_diffusion.originCell == origin_cell_test
    assert test_diffusion.targetCell == target_cell_test

    new_origin_cell_test = KMCmodel.cell.Cell(2, 2, 2)
    test_diffusion.originCell = new_origin_cell_test

    assert test_diffusion.originCell == new_origin_cell_test
    assert test_diffusion.targetCell == target_cell_test

    new_target_cell_test = KMCmodel.cell.Cell(3, 3, 3)
    test_diffusion.targetCell = new_target_cell_test

    assert test_diffusion.originCell == new_origin_cell_test
    assert test_diffusion.targetCell == new_target_cell_test

    test_diffusion.originCell = origin_cell_test
    test_diffusion.targetCell = target_cell_test

    assert test_diffusion.originCell == origin_cell_test
    assert test_diffusion.targetCell == target_cell_test

def test_diffusion_probability_getter():
    origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    test_diffusion = KMCmodel.diffusion.Diffusion(origin_cell_test, target_cell_test)

    assert test_diffusion.probability == 0

def test_diffusion_probability_setter():
    origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    test_diffusion = KMCmodel.diffusion.Diffusion(origin_cell_test, target_cell_test)

    assert test_diffusion.probability == 0

    test_diffusion.probability = 25
    assert test_diffusion.probability == 25

def test_diffusion_equals():
    origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    test_diffusion = KMCmodel.diffusion.Diffusion(origin_cell_test, target_cell_test)

    second_origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    second_target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    second_test_diffusion = KMCmodel.diffusion.Diffusion(second_origin_cell_test, second_target_cell_test)

    assert test_diffusion.equals(second_test_diffusion) == True

    new_second_origin_cell_test = KMCmodel.cell.Cell(2, 2, 2)
    second_test_diffusion.originCell = new_second_origin_cell_test
    
    assert test_diffusion.equals(second_test_diffusion) == False

    second_test_diffusion.originCell = second_origin_cell_test
    new_second_target_cell_test = KMCmodel.cell.Cell(3, 3, 3)
    second_test_diffusion.targetCell = new_second_target_cell_test

    assert test_diffusion.equals(second_test_diffusion) == False

    second_test_diffusion.targetCell = second_target_cell_test

    assert test_diffusion.equals(second_test_diffusion) == True

    second_test_diffusion.originCell = new_second_origin_cell_test
    second_test_diffusion.targetCell = new_second_target_cell_test

    assert test_diffusion.equals(second_test_diffusion) == False

    second_test_diffusion.originCell = second_origin_cell_test
    second_test_diffusion.targetCell = second_target_cell_test

    assert test_diffusion.equals(second_test_diffusion) == True

    test_diffusion.originCell = new_second_origin_cell_test

    assert test_diffusion.equals(second_test_diffusion) == False

    test_diffusion.originCell = origin_cell_test
    test_diffusion.targetCell = new_second_target_cell_test

    assert test_diffusion.equals(second_test_diffusion) == False

    test_diffusion.targetCell = target_cell_test

    assert test_diffusion.equals(second_test_diffusion) == True

    test_diffusion.originCell = new_second_origin_cell_test
    test_diffusion.targetCell = new_second_target_cell_test
    assert test_diffusion.equals(second_test_diffusion) == False

    test_diffusion.originCell = origin_cell_test
    test_diffusion.targetCell = target_cell_test

    assert test_diffusion.equals(second_test_diffusion) == True

    adsorption_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    test_adsorption = KMCmodel.adsorption.Adsorption(adsorption_cell_test, 0.49999999)

    assert test_diffusion.equals(test_adsorption) == False

def test_diffusion_cumulateProbability():
    origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    test_diffusion = KMCmodel.diffusion.Diffusion(origin_cell_test, target_cell_test)

    cumulated_probability = 0
    assert test_diffusion.calculateProbability(cumulated_probability) == 0
    assert test_diffusion.probability == 0

    second_origin_cell_test = KMCmodel.cell.Cell(0, 0, 0)
    second_target_cell_test = KMCmodel.cell.Cell(1, 1, 1)
    second_origin_cell_test.energy = 1
    second_target_cell_test.energy = 2
    second_test_diffusion = KMCmodel.diffusion.Diffusion(second_origin_cell_test, second_target_cell_test)
    assert second_test_diffusion.calculateProbability(cumulated_probability) != 0
    assert second_test_diffusion.probability != 0
