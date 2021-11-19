from typing import NamedTuple
import math

def calculate_fuel_list_from_mass_list(mass_list):
    pass

def calculate_fuel_needed_from_mass(mass):
    fuel_needed = (math.trunc(mass/3.0)) - 2
    return fuel_needed

class Module(NamedTuple):
    mass: int

# if __name__ == '__main__':
#     print_hi('PyCharm')

