import pytest

import KMCmodel.parameters

test_parameters = KMCmodel.parameters.Parameters()

def test_space_size_getter():
    assert test_parameters.space_size == 70

def test_space_size_setter():
    test_parameters.space_size = 1
    assert test_parameters.space_size == 1

def test_substrate_temperature_getter():
    assert test_parameters.substrate_temperature == 700

def test_substrate_temperature_setter():
    test_parameters.substrate_temperature = 1
    assert test_parameters.substrate_temperature == 1

def test_melting_temperature_getter():
    assert test_parameters.melting_temperature == 2930

def test_melting_temperature_setter():
    test_parameters.melting_temperature = 1
    assert test_parameters.melting_temperature == 1

def test_boltzman_constant_getter():
    assert test_parameters.boltzman_constant == 8.617333262 * 10e-5 

def test_boltzman_constant_setter():
    test_parameters.boltzman_constant = 1
    assert test_parameters.boltzman_constant == 1

def test_vibration_frequency_getter():
    assert test_parameters.vibration_frequency == 1e13

def test_vibration_frequency_setter():
    test_parameters.vibration_frequency = 1
    assert test_parameters.vibration_frequency == 1

def test_energyAA_getter():
    assert test_parameters.energyAA == 0.8

def test_energyAA_setter():
    test_parameters.energyAA = 1
    assert test_parameters.energyAA == 1

def test_energy_vapour_getter():
    assert test_parameters.energy_vapour == 1000

def test_energy_vapour_setter():
    test_parameters.energy_vapour = 1
    assert test_parameters.energy_vapour == 1

def test_cell_dim_getter():
    assert test_parameters.cell_dim == 1e-9

def test_cell_dim_setter():
    test_parameters.cell_dim = 1
    assert test_parameters.cell_dim == 1

def test_nano_second_getter():
    assert test_parameters.nano_second == 1e-9

def test_nano_second_setter():
    test_parameters.nano_second = 1
    assert test_parameters.nano_second == 1

def test_deposition_rate():
    result = 90.0e-9 / 1800.0
    assert test_parameters.deposition_rate == result


test_parameters2 = KMCmodel.parameters.Parameters()


def test_adsorption_probability():
    result = test_parameters2.deposition_rate / test_parameters2.cell_dim
    assert test_parameters2.adsorption_probability == result

def test_Tr():
    result = test_parameters2.substrate_temperature
    assert test_parameters2.Tr == result

def test_Tn():
    result = pow(test_parameters2.Tr, test_parameters2.n)
    assert test_parameters2.Tn == result

def test_kT():
    result = test_parameters2.Tr * test_parameters2.boltzman_constant
    assert test_parameters2.kT == result

def test_attempt_rate():
    result = test_parameters2.vibration_frequency
    assert test_parameters2.attempt_rate == result
