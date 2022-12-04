# --- Day 10 ---
#               _             _                                            
#      /\      | |           | |                /\                         
#     /  \   __| | __ _ _ __ | |_ ___ _ __     /  \   _ __ _ __ __ _ _   _ 
#    / /\ \ / _` |/ _` | '_ \| __/ _ \ '__|   / /\ \ | '__| '__/ _` | | | |
#   / ____ \ (_| | (_| | |_) | ||  __/ |     / ____ \| |  | | | (_| | |_| |
#  /_/    \_\__,_|\__,_| .__/ \__\___|_|    /_/    \_\_|  |_|  \__,_|\__, |
#                      | |                                            __/ |
#                      |_|                                           |___/ 

import os, sys


def load_input(filename):

    with open(filename) as f:
        input = []

        for line in f:
            input.append(int(line.strip()))

        return input


def part1(input):

    jolt_diff1 = 0
    jolt_diff3 = 0

    # count the number of times consecutive chargers have a jolt difference of either 1 or 3
    for i in range(1, len(input)):
        lower = input[i - 1]
        upper = input[i]
        
        jolt_diff = upper - lower 

        if jolt_diff == 1:
            jolt_diff1 += 1
        elif jolt_diff == 3:
            jolt_diff3 += 1

    # our answer is the number of jolt differences of 1 multiplied by the jolt differences of 3
    print(f'1:{jolt_diff1} 3:{jolt_diff3} 1*3:{jolt_diff1 * jolt_diff3}')


class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.children = []
        self.value = value

    def __str__(self):
        return self.value


def part2(input):
    # count the number of different ways these can be possibly be arranged. Essentially this means
    # we can skip some in certain cases (within the existing ruleset of jumps no more than 3). 
    # E.g. 
    # brute force is probably too slow here. 
    
    options_per_input = []

    for i in range(0, len(input) - 1):
        
        options = 1

        # guaranteed that it can connect to the next one - can it reach the 2 after?            
        if i + 3 < len(input) and input[i] + 3 >= input[i + 3]:
            options_per_input.append(3)
        elif i + 2 < len(input) and input[i] + 3 >= input[i + 2]:
            options_per_input.append(2)
        else:
            options_per_input.append(1)

    # since solutions converge where we only have 1 option, we can simplify our set down by 
    # removing consecutive 1s and forming into the 'groups' of higher numbers
    # e.g. 1 1 3 2 1 1 2 1
    # all we care about is (3, 2) (2). (3, 2) has 4 routes and (2) has 2, so multiple together to get... 8!
    route_groups = []
    current_group = []

    for i in options_per_input:
        if i == 1 and len(current_group) != 0:
            route_groups.append(current_group)
            current_group = []
            continue

        if i != 1:
            current_group.append(i)

    print(options_per_input)
    print(route_groups)

    # these groups can be (3, 3, 2) = 6 routes, (3, 2) = 4 routes, (2) = 2 routes
    multiplier = 1
    for i in route_groups:
        if len(i) == 3:
            multiplier *= 7
        elif len(i) == 2:
            multiplier *= 4
        else: 
            multiplier *= 2

    print(f'Lord that was a pain. Found {multiplier} different possible routes.')


if __name__ == "__main__":
    input = load_input('day10/day10_input.txt')
    # input = load_input('day10/day10_input_simple.txt')
    # input = load_input('day10/day10_input_simple2.txt')

    # add the charging outlet (0) and my device (max + 3) to the input
    input.append(0)
    input.append(max(input) + 3)

    # since we must use all devices, we can sort into order
    input.sort()

    # part1(input)
    part2(input)
