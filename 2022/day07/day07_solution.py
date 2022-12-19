# --- day07 ---
#     _   __         _____                          __         ______
#    / | / /___     / ___/____  ____ _________     / /   ___  / __/ /_
#   /  |/ / __ \    \__ \/ __ \/ __ `/ ___/ _ \   / /   / _ \/ /_/ __/
#  / /|  / /_/ /   ___/ / /_/ / /_/ / /__/  __/  / /___/  __/ __/ /_
# /_/ |_/\____/   /____/ .___/\__,_/\___/\___/  /_____/\___/_/  \__/
#                     /_/
#    ____           ____            _
#   / __ \____     / __ \___ _   __(_)_______
#  / / / / __ \   / / / / _ \ | / / / ___/ _ \
# / /_/ / / / /  / /_/ /  __/ |/ / / /__/  __/
# \____/_/ /_/  /_____/\___/|___/_/\___/\___/
#
#
from enum import Enum
from typing import Optional


class Dir:
    def __init__(self, parent_dir: Optional["Dir"]):
        self.parent_dir: Optional[Dir] = parent_dir
        self.children_dirs: dict[Dir] = {}
        self.files: dict[int] = {}
        self.total_size = None

    def add_file(self, name: str, size: int) -> None:
        self.files[name] = size

    def change_dir(self, name: str) -> "Dir":
        if name in self.children_dirs:
            return self.children_dirs[name]

        new_dir = Dir(parent_dir=self)
        self.children_dirs[name] = new_dir
        return new_dir


def get_file_structure(input) -> Dir:
    current_cmd = None
    root = Dir(parent_dir=None)
    cursor = root

    for line in input[1:]:
        # $ indicates a new command is being set
        current_cmd = line.split(" ")
        if line[0] == "$":

            if current_cmd[1] == "cd":
                target = current_cmd[2]
                if target == "..":
                    cursor = cursor.parent_dir if cursor.parent_dir else cursor
                else:
                    cursor = cursor.change_dir(target)
        else:
            # process ls output
            if current_cmd[0] != "dir":
                cursor.add_file(current_cmd[1], int(current_cmd[0]))
    
    return root


def print_structure(dir: Dir, depth: int = 0):
    padding = ''.join(['  ' for i in range(depth)])
    for x in dir.children_dirs.keys():
        print(padding + x + ":--")
        print_structure(dir.children_dirs[x], depth + 1)
    
    for x in dir.files.keys():
        print(f"{padding} - {x} ({dir.files[x]})")


all_dir_sizes = []
def calculate_sizes(dir: Dir, name: str, all_dir_sizes: list): 
    dir.total_size = sum(dir.files.values())

    for dir_name in dir.children_dirs.keys():
        child = dir.children_dirs[dir_name]
        calculate_sizes(child, dir_name, all_dir_sizes)
        dir.total_size += child.total_size

    all_dir_sizes.append(dir.total_size)

    
def load_input(filename):
    lines = []
    with open(filename) as f:
        while x := f.readline():
            lines.append(x.strip())
    return lines


def part1(input):
    root = get_file_structure(input)
    print_structure(root)
    all_dir_sizes = []
    calculate_sizes(root, "/", all_dir_sizes)
    sum_of_dirs_under_100k = sum([x for x in all_dir_sizes if x < 100000])
    print(sum_of_dirs_under_100k)


def part2(input):
    root = get_file_structure(input)
    print_structure(root)
    all_dir_sizes = []
    calculate_sizes(root, "/", all_dir_sizes)
    unused = 70000000 - all_dir_sizes[-1]
    required_space = 30000000 - unused
    print(unused, required_space)
    smallest_delete = sorted([x for x in all_dir_sizes if x >= required_space])[0]
    print(smallest_delete)


if __name__ == "__main__":
    dir = "/".join(__file__.split("/")[:-1])
    # input = load_input(dir + "/input_simple.txt")
    input = load_input(dir + '/input.txt')
    
    # part1(input)
    part2(input)
