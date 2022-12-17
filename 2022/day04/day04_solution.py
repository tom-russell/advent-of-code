# --- Day day04 ---
#    ______                         ________                           
#   / ____/___ _____ ___  ____     / ____/ /__  ____ _____  __  ______ 
#  / /   / __ `/ __ `__ \/ __ \   / /   / / _ \/ __ `/ __ \/ / / / __ \
# / /___/ /_/ / / / / / / /_/ /  / /___/ /  __/ /_/ / / / / /_/ / /_/ /
# \____/\__,_/_/ /_/ /_/ .___/   \____/_/\___/\__,_/_/ /_/\__,_/ .___/ 
#                     /_/                                     /_/      
# 
import os, sys


def load_input(filename):
    lines = []
    with open(filename) as f:
         while x:= f.readline():
            lines.append(x.strip())
    return lines


def line_parse(line):
    a = line.split(",")[0]
    b = line.split(",")[1]
    return (int(a.split("-")[0]), int(a.split("-")[1])), (int(b.split("-")[0]), int(b.split("-")[1]))


def part1(input):
    count = 0
    for line in input:
        a, b = line_parse(line)
        if (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1]):
            count += 1
    print(count)


def part2(input):
    count = 0
    for line in input:
        a, b = line_parse(line)
        if (a[0] >= b[0] and a[0] <= b[1]) or (b[0] >= a[0] and b[0] <= a[1]):
            count += 1
    print(count)



if __name__ == "__main__":
    # input = load_input('day04/day04_input_simple.txt')
    input = load_input('day04/day04_input.txt')

    # part1(input)
    part2(input)
