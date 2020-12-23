# --- Day 1  ---
#   _____                       _     _____                  _      
#  |  __ \                     | |   |  __ \                (_)     
#  | |__) |___ _ __   ___  _ __| |_  | |__) |___ _ __   __ _ _ _ __ 
#  |  _  // _ \ '_ \ / _ \| '__| __| |  _  // _ \ '_ \ / _` | | '__|
#  | | \ \  __/ |_) | (_) | |  | |_  | | \ \  __/ |_) | (_| | | |   
#  |_|  \_\___| .__/ \___/|_|   \__| |_|  \_\___| .__/ \__,_|_|_|   
#             | |                               | |                 
#             |_|                               |_|                 

import os, sys


def load_inputs_as_ints(filename: str) -> [int]:
    """Read the input file and return into a list of strings."""
    with open(filename) as f:
        content = f.read()
        return [int(x) for x in content.strip().split('\n')]
        return content.strip().split('\n')


def part1(inputs) -> int:
    # iterate through every combination of 2 inputs until we find the combination 
    # that sums to 2020
    for i in range (0, len(inputs)):
        for j in range (0, len(inputs)):
            # we need 2 unique inputs
            if i == j:
                continue
            
            entry1 = inputs[i]
            entry2 = inputs[j]

            if entry1 + entry2 == 2020:

                print(f'Solution Found: indexes {i}:{entry1} + {j}:{entry2}')
                print(f'{entry1} + {entry2} = {entry1 + entry2}')
                print(f'Answer = {entry1} * {entry2} = {entry1 * entry2}')
                exit()

    # no valid combination found, either invalid input or bad code :(
    print('Error - No valid combination found')
    exit(1)


def part2(inputs) -> int:
    # iterate through every combination of 3 inputs until we find the combination 
    # that sums to 2020
    for i in range (0, len(inputs)):
        for j in range (0, len(inputs)):
            for k in range (0, len(inputs)):
                # we need 3 unique inputs
                if i == j or i == k or j == k:
                    continue
                
                entry1 = inputs[i]
                entry2 = inputs[j]
                entry3 = inputs[k]

                if entry1 + entry2 + entry3 == 2020:

                    print(f'Solution Found: indexes {i}:{entry1} + {j}:{entry2} + {k}:{entry3}')
                    print(f'{entry1} + {entry2} + {entry3} = {entry1 + entry2 + entry3}')
                    print(f'Answer = {entry1} * {entry2} * {entry3} = {entry1 * entry2 * entry3}')
                    exit()

    # no valid combination found, either invalid input or bad code :(
    print('Error - No valid combination found')
    exit(1)


if __name__ == "__main__":
    inputs = load_inputs_as_ints('day1/day1_input.txt')

    part1(inputs)
    #part2(inputs)
