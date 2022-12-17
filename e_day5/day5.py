import os
from pathlib import Path
from collections import deque


def solve_puzzle(inp, part_one):
    # each "column" in the input file is "    " or "[X] ", so figure out the initial stacks that way
    # also, they're 1-indexed
    stack_count = (len(inp[0]) // 4) + 2
    stacks = {i: deque() for i in range(stack_count)}
    for row in inp:
        if "[" in row:
            for i in range(0, len(row), 4):
                if "[" in row[i : i + 3]:
                    stacks[(i // 4) + 1].appendleft(row[i + 1])
        elif "move" in row:
            to_move, move_from, move_to = [
                int(i) for i in row.split(" ") if i.isnumeric()
            ]
            if part_one:
                for _ in range(to_move):
                    stacks[move_to].append(stacks[move_from].pop())
            else:
                moving = []
                for _ in range(to_move):
                    moving.append(stacks[move_from].pop())
                for crate in reversed(moving):
                    stacks[move_to].append(crate)
    solution = "".join(stacks[i].pop() for i in range(1, stack_count))
    if part_one:
        print(f"Part one (which crates are on top of each stack):\n{solution}")
    else:
        print(f"Part two (which crates are on top for real):\n{solution}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    inp = Path(filepath).read_text().splitlines()
    solve_puzzle(inp, True)
    solve_puzzle(inp, False)
