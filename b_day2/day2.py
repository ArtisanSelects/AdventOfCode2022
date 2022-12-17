import os
from pathlib import Path

shape_points = {"X": 1, "Y": 2, "Z": 3}
draw_outcomes = {"X": "A", "Y": "B", "Z": "C"}
winning_outcomes = {"X": "C", "Y": "A", "Z": "B"}
losing_outcomes = {"X": "B", "Y": "C", "Z": "A"}
draw_points = 3
win_points = 6


def solve_part_one(rounds):
    res = 0
    for round in rounds:
        elf_move, my_move = round.split(" ")
        res += shape_points[my_move]
        if draw_outcomes[my_move] == elf_move:
            res += draw_points
        elif winning_outcomes[my_move] == elf_move:
            res += win_points
    print(f"Part one (strategy guide points total):\n{res}")


def solve_part_two(rounds):
    res = 0
    outcomes = {
        "X": {v: k for k, v in losing_outcomes.items()},
        "Y": {v: k for k, v in draw_outcomes.items()},
        "Z": {v: k for k, v in winning_outcomes.items()},
    }
    outcome_points = {"X": 0, "Y": 3, "Z": 6}
    for round in rounds:
        elf_move, outcome = round.split(" ")
        shape = outcomes[outcome][elf_move]
        res += outcome_points[outcome] + shape_points[shape]
    print(f"Part two (strategy guide with outcomes):\n{res}")


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    rounds = Path(filepath).read_text().splitlines()
    solve_part_one(rounds)
    solve_part_two(rounds)
