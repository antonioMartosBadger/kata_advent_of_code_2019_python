import unittest

from main import Exercise1


class TestExercise1(unittest.TestCase):

    def test_calculate_fuel_needed_from_mass(self):
        mass = 14
        expected_fuel_needed = 2

        exercise1 = Exercise1()
        fuel_needed = exercise1.calculate_fuel_needed_from_mass(mass)

        self.assertEqual(fuel_needed, expected_fuel_needed)

    def test_calculate_fuel_list_from_mass_list(self):
        mass_list = [12, 14, 1969, 100756]
        expected_fuel_list = [2, 2, 654, 33583]

        exercise1 = Exercise1()
        fuel_list = exercise1.calculate_fuel_list_from_mass_list(mass_list)
        self.assertEqual(expected_fuel_list, fuel_list)


