import pytest

import KMCmodel.adsorption
import KMCmodel.cell
import KMCmodel.parameters

test_cell = KMCmodel.cell.Cell(1,1,1)

test_adsorption = KMCmodel.adsorption.Adsorption(test_cell)

test_parameters = KMCmodel.parameters.Parameters()

def test_adsorption_creation_and_cell_getter():
    assert test_adsorption.cell == test_cell

def test_adsorption_creation_and_probability_test():
    assert test_adsorption.probability == test_parameters.adsorption_probability