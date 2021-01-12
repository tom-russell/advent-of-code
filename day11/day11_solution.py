# --- Day 11 ---
#    _____            _   _                _____           _                 
#   / ____|          | | (_)              / ____|         | |                
#  | (___   ___  __ _| |_ _ _ __   __ _  | (___  _   _ ___| |_ ___ _ __ ___  
#   \___ \ / _ \/ _` | __| | '_ \ / _` |  \___ \| | | / __| __/ _ \ '_ ` _ \ 
#   ____) |  __/ (_| | |_| | | | | (_| |  ____) | |_| \__ \ ||  __/ | | | | |
#  |_____/ \___|\__,_|\__|_|_| |_|\__, | |_____/ \__, |___/\__\___|_| |_| |_|
#                                  __/ |          __/ |                      
#                                 |___/          |___/                       

import os, sys


set_of_directions = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (1, -1), (1, 0), (1, +1)]


def load_input(filename):
    array2D = []
    with open(filename) as f:
        for line in f:
            array2D.append(list(line.strip()))

    return array2D


def pretty_print(input):
    occupied_count = 0
    for y in range(0, len(input)):
        occupied_count += input[y].count('#')
        print(' '.join(input[y]))

    print(f'{occupied_count} seats were occupied.')


def is_in_bounds(input, y, x):
    if x < 0 or y < 0:
        return False
    
    if y >= len(input) or x >= len(input[0]):
        return False

    return True
    

def count_adjacent_occupied(input, y, x):
    max_y = len(input)
    max_x = len(input[0])
    
    occupied_count = 0

    for dir in set_of_directions:
        if is_in_bounds(input, y + dir[0], x + dir[1]) and input[y + dir[0]][x + dir[1]] == '#':
            occupied_count += 1
    
    return occupied_count


def do_iteration_part1(input):
    new_input = []
    changes = 0

    for y in range(0, len(input)):
        new_input.append([])

        for x in range(0, len(input[y])):

            # an empty seat with no occupied seats adjacent becomes occupied
            if input[y][x] == 'L' and count_adjacent_occupied(input, y, x) == 0:
                new_input[y].append('#')
                changes += 1
                continue
            
            # an occupied seat with 4 or more adjacent seats occupied becomes empty
            elif input[y][x] == '#' and count_adjacent_occupied(input, y, x) >= 4:
                new_input[y].append('L')
                changes += 1
                continue

            # for any other case the seat or floor stays unchanged
            new_input[y].append(input[y][x])

    return new_input, changes


def part1(input):
    changes = 1
    iterations = 0

    # keep iterating until the seating plan reaches equilibrium
    while changes != 0:
        iterations += 1
        input, changes = do_iteration_part1(input)
        
    pretty_print(input)
    print(f'Took {iterations} iterations to reach equilibrium')


# return 
def is_seat_occupied_in_direction(input, y, x, dir):
    """Searches for the first seat from the given seat coordinate, in the given direction. 
    Returns True if that seat is occupied.
    """
    max_y = len(input)
    max_x = len(input[0])

    y += dir[0]
    x += dir[1]

    # keep checking in the eyeline direction until we either hit the seat, or get out of bounds
    while is_in_bounds(input, y, x):
        if input[y][x] == 'L':
            return False
        
        if input[y][x] == '#':
            return True

        y += dir[0]
        x += dir[1]

    return False


def count_occupied_in_eyeline(input, y, x):
    """Determines the number of occupied seats that are visible from the given seat coordinate."""
    count = 0
    for dir in set_of_directions:
        if is_seat_occupied_in_direction(input, y, x, dir):
            count += 1

    return count


def do_iteration_part2(input):
    new_input = []
    changes = 0

    for y in range(0, len(input)):
        new_input.append([])

        for x in range(0, len(input[y])):
            occupied_seats_in_eyeline = count_occupied_in_eyeline(input, y, x)

            # an empty seat with no occupied seats within eyeshot becomes occupied
            if input[y][x] == 'L' and occupied_seats_in_eyeline == 0:
                new_input[y].append('#')
                changes += 1
                continue
            
            # an occupied seat with 5 or more occupied seats in eyeshot becomes empty
            elif input[y][x] == '#' and occupied_seats_in_eyeline >= 5:
                new_input[y].append('L')
                changes += 1
                continue

            # for any other case the seat or floor stays unchanged
            new_input[y].append(input[y][x])

    return new_input, changes


def part2(input):
    changes = 1
    iterations = 0

    # keep iterating until the seating plan reaches equilibrium
    while changes != 0:
        iterations += 1
        input, changes = do_iteration_part2(input)
        
    pretty_print(input)
    print(f'Took {iterations} iterations to reach equilibrium')


if __name__ == "__main__":
    input = load_input('day11/day11_input.txt')

    # part1(input)
    part2(input)
