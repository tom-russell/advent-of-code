# --- day08 ---
#   ______               __                 ______             
#  /_  __/_______  ___  / /_____  ____     /_  __/_______  ___ 
#   / / / ___/ _ \/ _ \/ __/ __ \/ __ \     / / / ___/ _ \/ _ \
#  / / / /  /  __/  __/ /_/ /_/ / /_/ /    / / / /  /  __/  __/
# /_/ /_/   \___/\___/\__/\____/ .___/    /_/ /_/   \___/\___/ 
#                             /_/                              
#     __  __                    
#    / / / /___  __  __________ 
#   / /_/ / __ \/ / / / ___/ _ \
#  / __  / /_/ / /_/ (__  )  __/
# /_/ /_/\____/\__,_/____/\___/ 
#                               
# 

def load_input(filename):
    lines = []
    with open(filename) as f:
         while x:= f.readline():
            lines.append(x.strip())
    return lines


def parse_grid(input):
    grid = []
    for line in input:
        row = []
        for value in line:
            row.append(int(value))
        grid.append(row)
    return grid


current_tree = (0, 0)
def print_grid(grid: list[list[str]], star: tuple[int, int]=(-1, -1)):
    global current_tree
    for y in range(0, len(grid)):
        row_out = ' '
        for x in range(0, len(grid[0])):
            val = str(grid[y][x])
            if star == (y, x):
                val = 'o'
            elif current_tree == (y, x):
                val = '*'

            row_out += val + ' '
        print(row_out)


def is_visible(grid, y, x, max_y, max_x, dir: tuple=(1, 0)) -> bool:
    next_y = y + dir[0]
    next_x = x + dir[1]
    print("NEXT TREE..")
    print_grid(grid, (next_y, next_x))
    next_height = grid[next_y][next_x]
    if next_height >= grid[y][x]:
        print("BLOCKED!!")
        return False
    
    if (y+dir[0] == max_y or x + dir[1] == max_x or 
        y+dir[0] == 0 or x + dir[1] == 0):
        print("VISIBLE!!")
        return True
    
    return is_visible(grid, next_y, next_x, max_y, max_x, dir)


def part1(grid):
    print_grid(grid)
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    
    perimeter = len(grid) * 2 + len(grid[0]) * 2 - 4
    interior_trees = 0


    for y in range(1, max_y):
        for x in range(1, max_x):
            print('--', x, y, '--')
            global current_tree
            current_tree = (y, x)
            if (is_visible(grid, y, x, max_y, max_x, (1, 0)) or 
               is_visible(grid, y, x, max_y, max_x, (0, 1)) or 
               is_visible(grid, y, x, max_y, max_x, (0, -1)) or 
               is_visible(grid, y, x, max_y, max_x, (-1, 0))):
                interior_trees += 1

    print(perimeter)
    print(interior_trees)
    print(perimeter + interior_trees)


def part2(grid):
    pass


if __name__ == "__main__":
    dir = '/'.join(__file__.split('/')[:-1])
    input = load_input(dir + '/input_simple.txt')
    # input = load_input(dir + '/input.txt')
    grid = parse_grid(input)
    part1(grid)
    # part2(grid)
