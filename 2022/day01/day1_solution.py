# --- Day 01 ---
#    _____      _            _         _____                  _   _             
#   / ____|    | |          (_)       / ____|                | | (_)            
#  | |     __ _| | ___  _ __ _  ___  | |     ___  _   _ _ __ | |_ _ _ __   __ _ 
#  | |    / _` | |/ _ \| '__| |/ _ \ | |    / _ \| | | | '_ \| __| | '_ \ / _` |
#  | |___| (_| | | (_) | |  | |  __/ | |___| (_) | |_| | | | | |_| | | | | (_| |
#   \_____\__,_|_|\___/|_|  |_|\___|  \_____\___/ \__,_|_| |_|\__|_|_| |_|\__, |
#                                                                          __/ |
#                                                                         |___/ 

import os, sys


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def part1(input):
    highest = 0
    current = 0

    for line in input:
        try:
            current += int(line)
        except ValueError:
            highest = max(highest, current)
            current = 0

    print(max(highest, current))


def part2(input):
    values = [0, 0, 0]
    current = 0

    for line in input:    
        try:
            current += int(line)
        except ValueError:
            values.append(current)
            values.sort()
            values.pop(0)
            current = 0
    
    values.append(current)
    values.sort()
    print(sum(values[1:]))

if __name__ == "__main__":
    input = load_input('day1_input.txt')

    # part1(input)
    part2(input)
