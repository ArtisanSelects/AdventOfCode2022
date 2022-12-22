import os
from pathlib import Path
from heapq import heapify, heappush, heappop


def convert_terrain(terrain):
    res = [[] for _ in range(len(terrain))]
    for y, row in enumerate(terrain):
        for x, char in enumerate(row):
            if char != "S" and char != "E":
                res[y].append(ord(char) - 97)
            else:
                if char == "S":
                    goal = (y, x)
                    res[y].append(0)
                else:
                    start = (y, x)
                    res[y].append(25)
    return res, goal, start


def get_fewest_steps(terrain, goals=None):
    terrain, goal, start = convert_terrain(terrain)
    if goals is None:
        goals = set([goal])
    visited = set()
    queue = []
    heapify(queue)
    heappush(queue, (0, start))
    adjacent_cells = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_x = len(terrain[0])
    max_y = len(terrain)
    while queue:
        steps, cur_cell = heappop(queue)
        if cur_cell in visited:
            continue
        visited.add(cur_cell)
        steps += 1
        for cell in adjacent_cells:
            new_cell = tuple(sum(i) for i in zip(cell, cur_cell))
            y, x = new_cell
            if y >= max_y or x >= max_x or y < 0 or x < 0:
                continue
            cur_y, cur_x = cur_cell
            if terrain[cur_y][cur_x] - terrain[y][x] <= 1:
                if new_cell in goals:
                    return steps
                heappush(queue, (steps, new_cell))
    return None


def solve_part_two(terrain):
    goals = []
    converted_terrain, *_ = convert_terrain(terrain)
    for y in range(len(terrain)):
        for x in range(len(terrain[0])):
            if converted_terrain[y][x] == 0:
                goals.append((y, x))
    return get_fewest_steps(terrain, set(goals))


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    terrain = Path(filepath).read_text().splitlines()
    part_one = get_fewest_steps(terrain)
    print(f"Part one (fewest steps from start)\n{part_one}")
    part_two = solve_part_two(terrain)
    print(f"Part two (fewest steps from lowest starting points)\n{part_two}")
