# --- Day 2 ---
#   _____                                    _   _____  _     _ _                       _           
#  |  __ \                                  | | |  __ \| |   (_) |                     | |          
#  | |__) |_ _ ___ _____      _____  _ __ __| | | |__) | |__  _| | ___  ___  ___  _ __ | |__  _   _ 
#  |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | |  ___/| '_ \| | |/ _ \/ __|/ _ \| '_ \| '_ \| | | |
#  | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |    | | | | | | (_) \__ \ (_) | |_) | | | | |_| |
#  |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_|    |_| |_|_|_|\___/|___/\___/| .__/|_| |_|\__, |
#                                                                                | |           __/ |
#                                                                                |_|          |___/ 

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from utils import load_inputs_as_strings

def part1(inputs) -> int:
    valid_passwords = 0

    for line in inputs:
        # extract the password and requirements from the line
        # example line: 1-3 a: abcde
        required_char = line.split(' ')[1][0]  # the first character in the middle block
        min_occurrences = int(line.split(' ')[0].split('-')[0])  # the first number in the first block
        max_occurrences = int(line.split(' ')[0].split('-')[1])  # the second number in the first block
        password = line.split(' ')[2]

        # count up the occurrences of the required char 
        char_count = 0
        for char in password:
            char_count = char_count + 1 if char == required_char else char_count

        # password is valid if the character occurs the required number of times
        if char_count >= min_occurrences and char_count <= max_occurrences:
            valid_passwords += 1

    print(f'Found {valid_passwords} valid passwords. {len(inputs) - valid_passwords} were invalid.')


def part2(inputs) -> int:
    valid_passwords = 0

    for line in inputs:
        # extract the password and requirements from the line
        # example line: 1-3 a: abcde
        required_char = line.split(' ')[1][0]  # the first character in the middle block
        index1 = int(line.split(' ')[0].split('-')[0]) - 1  # the first number in the first block
        index2 = int(line.split(' ')[0].split('-')[1]) - 1  # the second number in the first block
        password = line.split(' ')[2]

        # password is valid if the char is present in ONLY 1 of the two indexes
        char_in_index1 = password[index1] == required_char
        char_in_index2 = password[index2] == required_char
        if char_in_index1 and not char_in_index2 or not char_in_index1 and char_in_index2:
            print(f'VALID!: {line}')
            valid_passwords += 1
        else:
            print(f'BIG OOFIES!: {line}')

    print(f'Found {valid_passwords} valid passwords. {len(inputs) - valid_passwords} were invalid.')


if __name__ == "__main__":
    inputs = load_inputs_as_strings('day2/day2_input.txt')

    part1(inputs)
    #part2(inputs)
