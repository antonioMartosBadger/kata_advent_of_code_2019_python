import unittest

from exercise1 import Module, calculate_fuel_needed_from_mass, calculate_fuel_list_from_mass_list

class TestExercise1(unittest.TestCase):

    def test_given_a_module_with_a_mass_of_14_when_calculating_fuel_needed_then_the_fuel_calculated_is_2(self):
        module = Module(mass=14)
        expected_fuel_needed = 2

        fuel_needed = calculate_fuel_needed_from_mass(module.mass)

        self.assertEqual(fuel_needed, expected_fuel_needed)

    def test_calculate_fuel_list_from_mass_list(self):
        mass_list = [12, 14, 1969, 100756]
        expected_fuel_list = [2, 2, 654, 33583]

        fuel_list = calculate_fuel_list_from_mass_list(mass_list)
        self.assertEqual(expected_fuel_list, fuel_list)


