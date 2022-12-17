import os
from pathlib import Path


def sign(res):
    return -1 if res < 0 else 1


def is_touching(new_head_pos, cur_tail_pos):
    for i in zip(new_head_pos, cur_tail_pos):
        if abs(i[1] - i[0]) > 1:
            return False
    return True


def handle_tail_movement(new_head_pos, cur_tail_pos):
    if is_touching(new_head_pos, cur_tail_pos):
        return cur_tail_pos

    new_x, new_y = cur_tail_pos
    x_diff = new_head_pos[0] - cur_tail_pos[0]
    y_diff = new_head_pos[1] - cur_tail_pos[1]

    if abs(x_diff) > 1:
        new_x += sign(x_diff)
        if y_diff != 0:
            new_y += sign(y_diff)
    elif abs(y_diff) > 1:
        new_y += sign(y_diff)
        if x_diff != 0:
            new_x += sign(x_diff)

    return (new_x, new_y)


def solve_puzzle(moves, knots):
    rope = [(0, 0) for _ in range(knots)]
    move_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    visited = set()
    for move in moves:
        dir, amount = move.split(" ")
        amount = int(amount)
        move = move_dict[dir]
        for _ in range(amount):
            rope[-1] = tuple(sum(i) for i in zip(rope[-1], move))
            for i in reversed(range(knots - 1)):
                rope[i] = handle_tail_movement(rope[i + 1], rope[i])
            visited.add(rope[0])
    return len(visited)


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    moves = Path(filepath).read_text().splitlines()
    part_one = solve_puzzle(moves, 2)
    print(f"Part one (tail positions with 2 knots):\n{part_one}")
    part_two = solve_puzzle(moves, 10)
    print(f"Part two (tail positions with 10 knots):\n{part_two}")
