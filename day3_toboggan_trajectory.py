# --- Day 3 ---
#   _______    _                                     _______        _           _                   
#  |__   __|  | |                                   |__   __|      (_)         | |                  
#     | | ___ | |__   ___   __ _  __ _  __ _ _ __      | |_ __ __ _ _  ___  ___| |_ ___  _ __ _   _ 
#     | |/ _ \| '_ \ / _ \ / _` |/ _` |/ _` | '_ \     | | '__/ _` | |/ _ \/ __| __/ _ \| '__| | | |
#     | | (_) | |_) | (_) | (_| | (_| | (_| | | | |    | | | | (_| | |  __/ (__| || (_) | |  | |_| |
#     |_|\___/|_.__/ \___/ \__, |\__, |\__,_|_| |_|    |_|_|  \__,_| |\___|\___|\__\___/|_|   \__, |
#                           __/ | __/ |                           _/ |                         __/ |
#                          |___/ |___/                           |__/                         |___/ 

from utils import load_input_as_2d_array


def get_trees_hit_count(input, x_velocity, y_velocity):
    """Input is the map, velocity is the (x, y) movement made each turn where y
    is down the slope and x is direction across the slope"""
    
    x = 0
    map_width = len(input[0])
    tree_count = 0

    for y in range(0 + y_velocity, len(input), y_velocity):
        # calculate the new x position
        x = x + x_velocity
        if x >= map_width:
            x = x - map_width

        # determine is a tree exists at this coordinate
        if input[y][x] == '#':
            tree_count = tree_count + 1

    print(f'With a velocity of ({x_velocity}, {y_velocity}) you reached the bottom, ' +
          f'hitting {tree_count} trees on the way. Ouch.')

    return tree_count


def part1(input):
    get_trees_hit_count(input, 3, 1)


def part2(input):
    velocities = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_count_multiplier = 1

    for velocity in velocities:
        tree_hit_count = get_trees_hit_count(input, velocity[0], velocity[1])
        tree_count_multiplier = tree_count_multiplier * tree_hit_count

    print(f'All the tree hits multiplied together give the answer: {tree_count_multiplier}')


if __name__ == "__main__":
    input = load_input_as_2d_array('day3_input.txt')
    
    # part1(input)
    part2(input)
