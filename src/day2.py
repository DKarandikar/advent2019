import copy

from src.input_helpers.read_intcode import parse_list_of_ints
from src.logic_helpers.intcode import IntCodeComputer


def main():
    program = parse_list_of_ints("../inputData/day2input")
    part1 = copy.deepcopy(program)
    part1[1] = 12
    part1[2] = 2
    computer = IntCodeComputer(part1, pad_program=False)
    _, __ = computer.run_until_input_or_done()
    print(f"Part 1 result is {computer.program[0]}")


if __name__ == "__main__":
    main()
