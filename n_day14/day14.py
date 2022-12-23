import os
from pathlib import Path


MOVES = [(0, 1), (-1, 1), (1, 1)]
SAND_START = (500, 0)


def parse_rocks(rocks):
    res = set()
    rocks = [i.split(" -> ") for i in rocks]
    for rock_line in rocks:
        cur_coord = None
        for rock in rock_line:
            x, y = list(map(int, rock.split(",")))
            if cur_coord is None:
                cur_coord = (x, y)
                continue
            cur_x, cur_y = cur_coord
            if cur_x == x:
                start = min(y, cur_y)
                end = max(y, cur_y) + 1
                res.update([(x, i) for i in range(start, end)])
            else:
                start = min(x, cur_x)
                end = max(x, cur_x) + 1
                res.update([(i, y) for i in range(start, end)])
            cur_coord = (x, y)
    return res


def move_sand(sand, rocks, max_y):
    for move in MOVES:
        new_position = tuple(sum(i) for i in zip(sand, move))
        if new_position not in rocks:
            x, y = new_position
            return (x, min(y, max_y))
    return sand


def solve_part(rocks, abyss_y, part_number):
    rocks_start_len = len(rocks)
    cur_sand = SAND_START
    if part_number == 1:
        wincon = lambda x: x[1] >= abyss_y
    else:
        abyss_y += 1
        wincon = lambda x: x == SAND_START
    while True:
        new_sand = move_sand(cur_sand, rocks, abyss_y)
        if wincon(new_sand):
            # draw_rocks(rocks, abyss_y)
            res = len(rocks) - rocks_start_len
            return res if part_number == 1 else res + 1
        if new_sand == cur_sand:
            rocks.add(new_sand)
            cur_sand = SAND_START
        else:
            cur_sand = new_sand


def draw_rocks(rocks, abyss_y):
    x_offset = min(i[0] for i in rocks)
    x_max = max(i[0] for i in rocks) - x_offset + 2
    for y in range(abyss_y + 2):
        row = []
        for x in range(x_max):
            row.append("#" if (x + x_offset, y) in rocks else ".")
        print("".join(row))


def solve_puzzle(rocks):
    rocks = parse_rocks(rocks)
    abyss_y = max(rock[1] for rock in rocks)
    part_one = solve_part(set(rocks), abyss_y, 1)
    print(f"Part one (how many steps until abyss)\n{part_one}")
    part_two = solve_part(set(rocks), abyss_y, 2)
    print(f"Part one (how many steps until sand stops)\n{part_two}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    rocks = Path(filepath).read_text().splitlines()
    solve_puzzle(rocks)
