from typing import NamedTuple

def calculate_fuel_list_from_mass_list(mass_list):
    pass

def calculate_fuel_needed_from_mass(mass):
    return 0 if mass < 6 else mass // 3.0 - 2

class Module(NamedTuple):
    mass: float

# if __name__ == '__main__':
#     print_hi('PyCharm')

