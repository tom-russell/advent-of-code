# --- Day X ---
#    _____          _                     _____          _                      
#   / ____|        | |                   / ____|        | |                     
#  | |    _   _ ___| |_ ___  _ __ ___   | |    _   _ ___| |_ ___  _ __ ___  ___ 
#  | |   | | | / __| __/ _ \| '_ ` _ \  | |   | | | / __| __/ _ \| '_ ` _ \/ __|
#  | |___| |_| \__ \ || (_) | | | | | | | |___| |_| \__ \ || (_) | | | | | \__ \
#   \_____\__,_|___/\__\___/|_| |_| |_|  \_____\__,_|___/\__\___/|_| |_| |_|___/                                                                 
                                                                            
import os, sys


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def part1(input):
    '''Identify the questions to which ANYONE answered "Yes"'''

    total_counts = 0
    group = set()

    for index in range(0, len(input) + 1):
        # an empty line or exceeded max index signifies the end of the current group
        if index == len(input) or input[index].strip() == '':
            total_counts += len(group)
            print(f'{total_counts}:{group}')
            group = set()
            continue

        # add each distinct answer for the group to a set
        for char in input[index].strip():
            group.add(char)

    print(f'Total count sum for all groups comes to: {total_counts}')


def part2(input):
    '''Identify the questions to which EVERYONE answered "Yes"'''
    
    all_groups = []  # list of all the answers from all the groups 
    group = []  # list represents a single group, each item a separate member 
    all_groups.append(group)

    # extract all the group data into a list of lists of strings for easier processing
    for index in range(0, len(input)):
        # an empty line signifies the end of the current group
        if input[index].strip() == '':
            group = []
            all_groups.append(group)
            continue

        # add this member to the group
        group.append(input[index].strip())

    # analyse the data
    total_counts = 0

    for group in all_groups:
        # a group with 1 member automatically all answer the same
        if len(group) == 1:
            total_counts += len(group[0])
            continue
            
        # since the answer must be present for all members, we can just check if the first members
        # answers are present for all other members
        for answer in group[0]:
            all_present = True

            for member in range(1, len(group)):
                if answer not in group[member]:
                   all_present = False
                   break
            
            if all_present:
                total_counts += 1
        

    print(f'Total count sum for all groups comes to: {total_counts}')


if __name__ == "__main__":  
    input = load_input('day6/day6_input.txt')
    # input = load_input('day6/day6_input_simple.txt')

    # part1(input)
    part2(input)
