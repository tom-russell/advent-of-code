# --- Day X ---
#   _    _                 _         _    _                                     _        
#  | |  | |               | |       | |  | |                                   | |       
#  | |__| | __ _ _ __   __| |_   _  | |__| | __ ___   _____ _ __ ___  __ _  ___| | _____ 
#  |  __  |/ _` | '_ \ / _` | | | | |  __  |/ _` \ \ / / _ \ '__/ __|/ _` |/ __| |/ / __|
#  | |  | | (_| | | | | (_| | |_| | | |  | | (_| |\ V /  __/ |  \__ \ (_| | (__|   <\__ \
#  |_|  |_|\__,_|_| |_|\__,_|\__, | |_|  |_|\__,_| \_/ \___|_|  |___/\__,_|\___|_|\_\___/
#                             __/ |                                                      
#                            |___/                                                       

import os, sys
import queue


shiny_gold = 'shiny gold'


def parse_input(filename):
    must_contain = {}
    can_be_contained_by = {}

    with open(filename) as f:
        for line in f:
            # strip the fullstop from the end, and split up the container bag from the contained
            split_line = line.strip()[:-1].split(' contain ')

            outer_bag = split_line[0][:-5]
            must_contain[outer_bag] = {}

            # contained bags are separated by commas and have 3 details - number, adjective and colour
            # Example: 5 shiny gold bags
            for inner_bag in split_line[1].split(', '):
                if inner_bag == 'no other bags':
                    continue

                parts = inner_bag.split(' ')
                count = int(parts[0])
                descriptor = f'{parts[1]} {parts[2]}'
                must_contain[outer_bag][descriptor] = count

                # populate the 'can be contained by' for each of the contained bags
                if descriptor not in can_be_contained_by:
                    can_be_contained_by[descriptor] = {}
                
                can_be_contained_by[descriptor][outer_bag] = count

    return must_contain, can_be_contained_by


def part1(can_be_contained_by):
    '''find all the bags which could eventually contain at least one 'shiny gold' bag. Eventually
    meaning recursive - if shiny gold can hold X which can hold Y, Y is valid.'''
    
    valid_containers = set()
    bag_queue = queue.Queue()

    # starting point is all bags that can immediately hold a gold bad
    for container_bag in can_be_contained_by[shiny_gold]:
        bag_queue.put(container_bag)

    while not bag_queue.empty():
        bag = bag_queue.get_nowait()
        valid_containers.add(bag)
        
        # some bags can't be put inside any other bags - these are 'top level'
        if bag not in can_be_contained_by:
            continue

        for container_bag in can_be_contained_by[bag]:
            bag_queue.put(container_bag)

    print(valid_containers)
    print(f'{len(valid_containers)} bags can eventually contain a shiny gold bag!')


def part2(must_contain):
    '''How many bags in total must be contained within a shiny gold bag?'''
    
    bag_total = 0
    bag_queue = queue.Queue()

    # add the gold bag to the queue, and iterate over adding all contained bags to the end of the queue
    # adding to the bag total each time
    bag_queue.put(shiny_gold)

    while not bag_queue.empty():
        bag = bag_queue.get_nowait()
        
        for contained_bag in must_contain[bag]:
            count = must_contain[bag][contained_bag]
            bag_total += must_contain[bag][contained_bag]

            for x in range(0, count):
                bag_queue.put(contained_bag)

    print(f'Your shiny gold bag must contain {bag_total} bags!')


if __name__ == "__main__":
    filename = 'day7/day7_input.txt'

    must_contain, can_be_contained_by = parse_input(filename)

    # part1(can_be_contained_by)
    part2(must_contain)
