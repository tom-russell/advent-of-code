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
    def __init__(self, parent_dir: Optional[dict]):
        self.parent_dir: Optional[Dir] = None
        self.children_dirs: dict[Dir] = {}
        self.files: dict[int] = {}

    def add_file(self, name: str, size: int) -> None:
        self.files[name] = size

    def change_dir(self, name: str) -> "Dir":
        if name in self.children_dirs:
            return self.children_dirs[name]

        new_dir = Dir(parent_dir=self)
        self.children_dirs[name] = new_dir
        return new_dir


def load_input(filename):
    lines = []
    with open(filename) as f:
        while x := f.readline():
            lines.append(x.strip())
    return lines


def part1(input):
    current_cmd = None
    root = Dir(parent_dir=None)
    cursor = root

    for line in input[1:]:
        # $ indicates a new command is being set
        current_cmd = line.split(" ")
        print(f"{current_cmd}")
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

    print("done!")


def part2(input):
    pass


if __name__ == "__main__":
    dir = "/".join(__file__.split("/")[:-1])
    input = load_input(dir + "/input_simple.txt")
    # input = load_input(dir + '/input.txt')

    part1(input)
    # part2(input)
