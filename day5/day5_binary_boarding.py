# --- Day 5 ---
#   ____  _                          ____                      _ _             
#  |  _ \(_)                        |  _ \                    | (_)            
#  | |_) |_ _ __   __ _ _ __ _   _  | |_) | ___   __ _ _ __ __| |_ _ __   __ _ 
#  |  _ <| | '_ \ / _` | '__| | | | |  _ < / _ \ / _` | '__/ _` | | '_ \ / _` |
#  | |_) | | | | | (_| | |  | |_| | | |_) | (_) | (_| | | | (_| | | | | | (_| |
#  |____/|_|_| |_|\__,_|_|   \__, | |____/ \___/ \__,_|_|  \__,_|_|_| |_|\__, |
#                             __/ |                                       __/ |
#                            |___/                                       |___/ 

import os, sys


def load_inputs_as_strings(filename: str) -> [str]:
    """Read the input file and return into a list of strings."""
    with open(filename) as f:
        content = f.read()
        return content.strip().split('\n')


def binary_partition(string, min, max):
    if len(string) == 0:
        return int(min)

    if string[0] == '0':
        # lower, so min stays the same and max drops to the midpoint
        midpoint = (max - min + 1) / 2 - 1
        return binary_partition(string[1:], min, min + midpoint)
    else:
        # upper, so min ups to the midpoint and max stays the same
        midpoint = (max - min + 1) / 2
        return binary_partition(string[1:], min + midpoint, max)


def get_seat_row_and_col(boarding_pass) -> int:
    # the row part is the first 7 characters, the column part is the last 3
    # for simplicity we convert both to the same format - 0/1 instead of F/B and L/R
    row_part = boarding_pass[:7].replace('F', '0').replace('B', '1')
    col_part = boarding_pass[7:].replace('L', '0').replace('R', '1')

    row = binary_partition(row_part, 0, 127)
    col = binary_partition(col_part, 0, 7)
    
    return row, col


def get_seat_id(row, col):
    return row * 8 + col


def part1(input):
    max_seat_id = 0

    for boarding_pass in input:
        row, col = get_seat_row_and_col(boarding_pass)
        seat_id = get_seat_id(row, col)
        print(f'{boarding_pass}: seat ID {seat_id}')
        max_seat_id = seat_id if seat_id > max_seat_id else max_seat_id

    print(f'\nThe highest seat ID was: {max_seat_id}')
    

def part2(input):
    # create a list of all possible seats
    seats = []

    for x in range (0, 128):
        for y in range (0, 8):
            seats.append((x, y))

    # keep track of all the seat ids for the supplied boarding passes 
    seat_ids = []   

    for boarding_pass in input:
        row, col = get_seat_row_and_col(boarding_pass)
        seat_ids.append(get_seat_id(row, col))

        # remove all the found seats, so only unused seats are remaining
        seats.remove((row, col))

    # determine the only unused seat with both neighbours in the list of seat ids
    for seat in seats:
        seat_id = get_seat_id(seat[0], seat[1])
        if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
            print(seat)
            print(f'Found your seat! Your seat ID is {seat_id}')


if __name__ == "__main__":
    input = load_inputs_as_strings('day5/day5_input.txt')

    # part1(input)
    part2(input)
