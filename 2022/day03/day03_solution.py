# --- Day day03 ---
#     ____             __                   __  
#    / __ \__  _______/ /___________ ______/ /__
#   / /_/ / / / / ___/ //_/ ___/ __ `/ ___/ //_/
#  / _, _/ /_/ / /__/ ,< (__  ) /_/ / /__/ ,<   
# /_/ |_|\__,_/\___/_/|_/____/\__,_/\___/_/|_|  
#                                               
#     ____                                    _            __  _           
#    / __ \___  ____  _________ _____ _____  (_)________ _/ /_(_)___  ____ 
#   / /_/ / _ \/ __ \/ ___/ __ `/ __ `/ __ \/ / ___/ __ `/ __/ / __ \/ __ \
#  / _, _/  __/ /_/ / /  / /_/ / /_/ / / / / (__  ) /_/ / /_/ / /_/ / / / /
# /_/ |_|\___/\____/_/   \__, /\__,_/_/ /_/_/____/\__,_/\__/_/\____/_/ /_/ 
#                       /____/                                             
# 
import os, sys


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def _priority_score(char: str) -> int:
    return ord(char) - 96 if char.islower() else ord(char) - 38


def part1(lines):
    sum = 0
    for line in lines:
        compartment_size = int(len(line) / 2)
        a = set(line[:compartment_size])
        b = set(line[compartment_size:])
        char = a.intersection(b).pop()
        
        priority = _priority_score(char)
        print(char, priority)
        sum += priority
    print(sum)


def part2(lines):
    sum = 0
    for i in range(0, len(lines), 3):
        a = set(lines[i])
        b = set(lines[i+1])
        c = set(lines[i+2])
        char = a.intersection(b).intersection(c).pop()
        
        priority = _priority_score(char)
        print(char, priority)
        sum += priority
    print(sum)


if __name__ == "__main__":
    # input = load_input('day03/day03_input_simple.txt')
    input = load_input('day03/day03_input.txt')
    lines = [line.strip() for line in input]
    # part1(lines)
    part2(lines)
