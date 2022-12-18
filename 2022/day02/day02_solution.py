# --- Day 02 ---
#     ____             __      ____
#    / __ \____  _____/ /__   / __ \____ _____  ___  _____
#   / /_/ / __ \/ ___/ //_/  / /_/ / __ `/ __ \/ _ \/ ___/
#  / _, _/ /_/ / /__/ ,<    / ____/ /_/ / /_/ /  __/ /
# /_/ |_|\____/\___/_/|_|  /_/    \__,_/ .___/\___/_/
#                                     /_/
#    _____      _
#   / ___/_____(_)_____________  __________
#   \__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/
#  ___/ / /__/ (__  |__  ) /_/ / /  (__  )
# /____/\___/_/____/____/\____/_/  /____/
#
#
import os
import sys

score_grid = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
    },
}



score_grid_2 = {
    "A": {
        "X": 0 + 3,
        "Y": 3 + 1,
        "Z": 6 + 2,
    },
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2,
        "Z": 6 + 3,
    },
    "C": {
        "X": 0 + 2,
        "Y": 3 + 3,
        "Z": 6 + 1,
    },
}

shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def part1(input):
    score = 0
    for line in input:
        line = line.strip().split(" ")
        score += score_grid[line[0]][line[1]]
        score += shape_score[line[1]]

    print(score)


def part2(input):
    score = 0
    for line in input:
        line = line.strip().split(" ")
        score += score_grid_2[line[0]][line[1]]

    print(score)


if __name__ == "__main__":
    input = load_input("day02/day02_input.txt")

    # part1(input)
    part2(input)
