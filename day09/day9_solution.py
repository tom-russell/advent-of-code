# --- Day 9 ---
#   ______                     _ _               ______                     
#  |  ____|                   | (_)             |  ____|                    
#  | |__   _ __   ___ ___   __| |_ _ __   __ _  | |__   _ __ _ __ ___  _ __ 
#  |  __| | '_ \ / __/ _ \ / _` | | '_ \ / _` | |  __| | '__| '__/ _ \| '__|
#  | |____| | | | (_| (_) | (_| | | | | | (_| | | |____| |  | | | (_) | |   
#  |______|_| |_|\___\___/ \__,_|_|_| |_|\__, | |______|_|  |_|  \___/|_|   
#                                         __/ |                             
#                                        |___/                              

import os, sys


def load_input(filename):

    with open(filename) as f:
        input = []

        for line in f:
            input.append(int(line.strip()))

        return input


def find_numbers_that_sum(input, preamble_length, index):
    # we can search for numbers that sum within the previous {preamble_length} numbers
    for i in range(index - preamble_length, index):
        for j in range(index - preamble_length, index):
            
            # not valid if the numbers are the same 
            if input[i] == input[j]:
                continue

            # the number is valid if any combination of previous numbers sum to equal the current number
            if input[i] + input[j] == input[index]:
                valid = True
                return (input[i], input[j])

    # if we can't find a combination then this number is invalid!
    return None


def part1(input, preamble_length):
    """After the preamble, find the first value in the list that doesn't satisfy the condition:
    
    "each number you receive should be the sum of any two of the 25 immediately previous numbers. 
    The two numbers will have different values, and there might be more than one such pair."
    """

    for index in range(preamble_length, len(input)):

        values = find_numbers_that_sum(input, preamble_length, index)

        if values == None:
            print(f'Index {index}, value {input[index]} was invalid.')
            return


def part2(input, invalid_index):
    """you must find a contiguous set of at least two numbers in your list which sum to the 
    invalid number from step 1.
    """
    invalid_value = input[invalid_index]

    for i in range(0, invalid_index):

        # calculate the possible contiguous sets from the current index i - if we exceed the 
        # invalid value then this set is incorrect
        sum = 0
        sum_index = i + 1
        while sum < invalid_value:
            sum += input[sum_index]
                        
            # the valid set must sum to our 'invalid value'
            if sum == invalid_value:
                print(f'Valid set found! indexes {i}-{sum_index}')
                print(input[i:sum_index])
                min_from_set = min(input[i:sum_index])
                max_from_set = max(input[i:sum_index])
                print(f'min:{min_from_set} max:{max_from_set} minmaxsum:{min_from_set + max_from_set}')
                return

            sum_index += 1

    raise RuntimeError('No valid set found!')
            

if __name__ == "__main__":
    input = load_input('day9/day9_input.txt')

    # part1(input, preamble_length=25)
    part2(input, invalid_index=616)
