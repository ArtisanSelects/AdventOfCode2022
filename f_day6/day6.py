import os
from pathlib import Path
from collections import deque


def solve_puzzle(datastream, distinct_character_count):
    marker = 0 + distinct_character_count
    for i in range(len(datastream) - distinct_character_count - 1):
        if (
            len(set(datastream[i : i + distinct_character_count]))
            == distinct_character_count
        ):
            return marker
        marker += 1
    raise Exception(
        f"Failed to find the marker with distinct character count of {distinct_character_count}."
    )


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    datastream = Path(filepath).read_text().splitlines()[0]
    part_one = solve_puzzle(datastream, 4)
    part_two = solve_puzzle(datastream, 14)
    print(f"Part one (start-of-packet marker):\n{part_one}")
    print(f"Part two (start-of-message marker):\n{part_two}")
