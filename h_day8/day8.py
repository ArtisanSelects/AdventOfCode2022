import os
from pathlib import Path


def check_visibility(x, y, trees):
    height = trees[y][x]
    if max(trees[y][:x]) < height or max(trees[y][x+1:]) < height:
        return 1
    column = [trees[i][x] for i in range(len(trees))]
    if max(column[:y]) < height or max(column[y+1:]) < height:
        return 1
    return 0


def get_scenic_score(x, y, trees):
    def calc_scenic_score(height, row):
        res = 0
        for tree in row:
            res += 1
            if tree >= height:
                break
        return res

    height = trees[y][x]
    res = calc_scenic_score(height, reversed(trees[y][:x])) #left
    if res == 0:
        return res
    res *= calc_scenic_score(height, trees[y][x+1:]) #right
    if res == 0:
        return res
    column = [trees[i][x] for i in range(len(trees))]
    res *= calc_scenic_score(height, reversed(column[:y])) #up
    if res == 0:
        return res
    res *= calc_scenic_score(height, column[y+1:]) #down
    return res


def solve_puzzle(trees):
    y_len = len(trees)
    x_len = len(trees[0])
    res_part_one = (x_len*2)+((y_len-2)*2)
    res_part_two = 0
    for y in range(1, y_len-1):
        for x in range(1, x_len-1):
            res_part_one += check_visibility(x, y, trees)
            res_part_two = max(res_part_two, get_scenic_score(x, y, trees))
    print(f'Part one (number of visibile trees):\n{res_part_one}')
    print(f'Part two (max scenic score):\n{res_part_two}')
    

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    forest = Path(filepath).read_text().splitlines()
    trees = []
    for row in forest:
        trees.append([int(i) for i in list(row)])
    solve_puzzle(trees)