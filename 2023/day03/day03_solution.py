# --- day03 ---
#    ______                   ____        __  _
#   / ____/__  ____ ______   / __ \____ _/ /_(_)___  _____
#  / / __/ _ \/ __ `/ ___/  / /_/ / __ `/ __/ / __ \/ ___/
# / /_/ /  __/ /_/ / /     / _, _/ /_/ / /_/ / /_/ (__  )
# \____/\___/\__,_/_/     /_/ |_|\__,_/\__/_/\____/____/
#
#

import math

def load_input(filename):
    lines = []
    with open(filename) as f:
        while x := f.readline():
            lines.append(x.strip())
    return lines


class PartNumber:
    def __init__(self, number: int, row: int, column: int) -> None:
        self.number = number
        self.row = row
        self.column = column
        self.length = len(str(number))

    def surrounding_coordinates(self) -> set[tuple[int]]:
        coords = set()
        l_col = self.column - 1
        r_col = self.column + self.length
        coords.add((self.row, l_col))
        coords.add((self.row, r_col))
        for i in range(l_col, r_col + 1):
            coords.add((self.row - 1, i))
            coords.add((self.row + 1, i))

        return coords

    def __repr__(self) -> str:
        return f"{self.number} @ ({self.row}, {self.column})"


def part1(input):
    part_numbers: list[PartNumber] = []
    symbols: set[tuple[int]] = set()

    for row, line in enumerate(input):
        number = ""
        for column, character in enumerate(line):
            if character.isnumeric():
                number += character
            elif number:
                part_numbers.append(PartNumber(int(number), row, column - len(number)))
                number = ""

            if not character.isnumeric() and character != ".":
                symbols.add((row, column))

        if number:
            part_numbers.append(PartNumber(int(number), row, column + 1 - len(number)))

    sum = 0
    for part_number in part_numbers:
        if part_number.surrounding_coordinates() & symbols:
            sum += part_number.number

    print(sum)


def part2(input):
    part_numbers: list[PartNumber] = []
    stars: dict[tuple[int], list[int]] = {}

    for row, line in enumerate(input):
        number = ""
        for column, character in enumerate(line):
            if character.isnumeric():
                number += character
            elif number:
                part_numbers.append(PartNumber(int(number), row, column - len(number)))
                number = ""

            if character == "*":
                stars[(row, column)] = []

        if number:
            part_numbers.append(PartNumber(int(number), row, column + 1 - len(number)))

    star_set = set(stars)
    for part_number in part_numbers:
        for star_coord in part_number.surrounding_coordinates() & star_set:
            stars[star_coord].append(part_number.number)

    gear_ratio_sum = 0
    for gear_part_numbers in stars.values():
        if len(gear_part_numbers) == 2:
            gear_ratio_sum += math.prod(gear_part_numbers)
    print(gear_ratio_sum)


if __name__ == "__main__":
    dir = "/".join(__file__.split("/")[:-1])
    # input = load_input(dir + "/input_simple.txt")
    input = load_input(dir + "/input.txt")

    # part1(input)
    part2(input)
