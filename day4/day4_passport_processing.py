# --- Day 4 ---
#   _____                               _     _____                             _
#  |  __ \                             | |   |  __ \                           (_)
#  | |__) |_ _ ___ ___ _ __   ___  _ __| |_  | |__) | __ ___   ___ ___  ___ ___ _ _ __   __ _
#  |  ___/ _` / __/ __| '_ \ / _ \| '__| __| |  ___/ '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |
#  | |  | (_| \__ \__ \ |_) | (_) | |  | |_  | |   | | | (_) | (_|  __/\__ \__ \ | | | | (_| |
#  |_|   \__,_|___/___/ .__/ \___/|_|   \__| |_|   |_|  \___/ \___\___||___/___/_|_| |_|\__, |
#                     | |                                                                __/ |
#                     |_|                                                               |___/

import re


def load_input(filename: str):
    """Read the input file and return into a list of dictionaries, where each
    dictionary is a single passport with the keys/values holding the data.

    Passport data in the input may or may not be spread over multiple lines. A
    double line-break indicates a new passport entry.
    """
    passports = []

    with open(filename) as f:

        passport = {}

        for line in f:
            line = line.strip()

            # a blank line means the end of the current passport data
            if line == '':
                passports.append(passport)
                passport = {}
                continue

            data_items = {x.split(':')[0]: x.split(':')[1]
                          for x in line.split(' ')}
            passport = passport | data_items

    # in case there's no newline at the end of the file, check if the last passport has been added
    if len(passport) > 0:
        passports.append(passport)

    return passports


def part1(input):
    required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    valid_passport_count = 0

    for passport in input:
        print(passport)
        # if all the required fields are present as data items for the passport, it is valid
        if set(passport.keys()).issuperset(required_fields):
            valid_passport_count = valid_passport_count + 1

    print(f'Found {valid_passport_count} valid passports.')


def valid_range(number: str, min, max):
    return int(number) >= min and int(number) <= max


def part2(input):
    required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    valid_passport_count = 0

    for passport in input:
        # all fields must be present and valid
        print(passport)

        # passport must contain all of the required fields
        if not set(passport.keys()).issuperset(required_fields):
            continue

        # birth year, issue year, expiration year must fall within specific ranges
        if not valid_range(passport['byr'], 1920, 2002) or \
           not valid_range(passport['iyr'], 2010, 2020) or \
           not valid_range(passport['eyr'], 2010, 2030):
            continue

        # height must end with cm or in, and fall within certain ranges
        height = passport['hgt']

        if len(height) < 2 or \
           height[-2:] not in ('cm', 'in') or \
           height[-2:] == 'cm' and not valid_range(height[:-2], 150, 193) or \
           height[-2:] == 'in' and not valid_range(height[:-2], 59, 76):
            continue

        # hair colour must follow a specific formula
        if re.fullmatch('#[a-f0-9]{6}', passport['hcl']) is None:
            continue

        # eye colour must be one of several valid values
        if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue

        # passport ID must be a nine-digit number, leading zeroes are valid
        if re.fullmatch('[0-9]{9}', passport['pid']) is None:
            continue

        valid_passport_count = valid_passport_count + 1

    print(f'Found {valid_passport_count} valid passports.')


if __name__ == "__main__":
    input = load_input('day4/day4_input.txt')

    # part1(input)
    part2(input)
