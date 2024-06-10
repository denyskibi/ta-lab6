# Standard Libraries
from typing import Set


def load_unique_numbers_from_txt_file(file_path: str) -> Set[int]:
    unique_numbers = set()

    # Reading an input file and storing unique numbers in a set
    with open(file_path, 'r') as file:
        for line in file:
            number_str = line.strip()
            number = int(number_str)
            unique_numbers.add(number)

    return unique_numbers
