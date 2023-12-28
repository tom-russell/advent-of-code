import math

# --- day02 ---
#    ______      __
#   / ____/_  __/ /_  ___
#  / /   / / / / __ \/ _ \
# / /___/ /_/ / /_/ /  __/
# \____/\__,_/_.___/\___/
#
#    ______                            __
#   / ____/___  ____  __  ______  ____/ /______  ______ ___
#  / /   / __ \/ __ \/ / / / __ \/ __  / ___/ / / / __ `__ \
# / /___/ /_/ / / / / /_/ / / / / /_/ / /  / /_/ / / / / / /
# \____/\____/_/ /_/\__,_/_/ /_/\__,_/_/   \__,_/_/ /_/ /_/
#
#


class Round:
    def __init__(self, input: str) -> None:
        self.r = self.g = self.b = 0
        for colour in input.split(", "):
            if colour.endswith("red"):
                self.r = int(colour.split(" ")[0])
            if colour.endswith("green"):
                self.g = int(colour.split(" ")[0])
            if colour.endswith("blue"):
                self.b = int(colour.split(" ")[0])

    def __repr__(self) -> str:
        return f"Round {self.r}R {self.g}G {self.b}B"

    def is_valid(self):
        if self.r > 12 or self.g > 13 or self.b > 14:
            return False
        return True


class Game:
    def __init__(self, line: str):
        self.id = int(line.split(": ")[0][5:])
        self.rounds = [
            Round(round_str) for round_str in line.split(": ")[1].split("; ")
        ]

    def __repr__(self):
        return f"Game {self.id}: {self.rounds}"

    def is_valid(self):
        return all(round.is_valid() for round in self.rounds)

    def game_power(self):
        minimum_colours = [
            max(round.r for round in self.rounds),
            max(round.g for round in self.rounds),
            max(round.b for round in self.rounds),
        ]
        return math.prod(minimum_colours)


def load_input(filename):
    lines = []
    with open(filename) as f:
        while x := f.readline():
            lines.append(x.strip())
    return lines


def part1(input):
    sum = 0
    for game_str in input:
        game = Game(game_str)
        print(f"{game.id}: {game.is_valid()}")
        if game.is_valid():
            sum += game.id

    print(sum)


def part2(input):
    sum = 0
    for game_str in input:
        game = Game(game_str)
        print(f"{game.id}: {game.game_power()}")
        sum += game.game_power()

    print(sum)


if __name__ == "__main__":
    dir = "/".join(__file__.split("/")[:-1])
    # input = load_input(dir + "/input_simple.txt")
    input = load_input(dir + "/input.txt")

    # part1(input)
    part2(input)
