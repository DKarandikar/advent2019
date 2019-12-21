from typing import List


def parse_list_of_ints(filename: str) -> List[int]:
    with open(filename, "r") as f:
        string_numbers = f.readline().split(",")
        rv = [int(s) for s in string_numbers]

    return rv
