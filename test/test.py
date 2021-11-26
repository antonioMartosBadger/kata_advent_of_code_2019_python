import unittest

from exercise1 import Module, calculate_fuel_needed_from_mass, calculate_fuel_list_from_mass_list

class TestExercise1(unittest.TestCase):

    def test_given_a_module_with_a_mass_of_14_when_calculating_fuel_needed_then_the_fuel_calculated_is_2(self):
        module = Module(mass=14)
        expected_fuel_needed = 2

        fuel_needed = calculate_fuel_needed_from_mass(module.mass)

        self.assertEqual(fuel_needed, expected_fuel_needed)

    def test_when_mass_lower_than_6_then_the_fuel_calculated_result_is_zero(self):
        module = Module(mass=1)
        expected_fuel_needed = 0

        fuel_needed = calculate_fuel_needed_from_mass(module.mass)

        self.assertEqual(expected_fuel_needed, fuel_needed)

    def test_when_mass_is_negative_then_the_fuel_calculated_result_is_zero(self):
        module = Module(mass=-1)
        expected_fuel_needed = 0

        fuel_needed = calculate_fuel_needed_from_mass(module.mass)

        self.assertEqual(expected_fuel_needed, fuel_needed)

    def test_when_mass_has_decimals_then_the_fuel_calculated_result_is_zero(self):
        module = Module(mass=7.5)
        expected_fuel_needed = 0

        fuel_needed = calculate_fuel_needed_from_mass(module.mass)

        self.assertEqual(expected_fuel_needed, fuel_needed)

    def test_when_mass_has_zero_then_the_fuel_calculated_result_is_zero(self):
        module = Module(mass=0)
        expected_fuel_needed = 0

        fuel_needed = calculate_fuel_needed_from_mass(module.mass)

        self.assertEqual(expected_fuel_needed, fuel_needed)

    def test_given_a_modules_list_when_calculate_fuel_list_then_a_fuel_amount_list_is_returned(self):
        modules = [Module(12)]
        expected_fuels = [2]

        exercise1 = exercise1
        #Research how to Mock the method called via "calculate_fuels_from_modules"
        fuels = calculate_fuels_from_modules(modules)
        self.assertEqual(expected_fuels, fuels)
