from src.input_helpers.input_path import get_input_file
from src.input_helpers.read_intcode import parse_list_of_ints
from src.logic_helpers.intcode import IntCodeComputer


class TestAdditionMultiplication():
    def test_day_2_example_1(self):
        rv = parse_list_of_ints(get_input_file("day2test1"))
        computer = IntCodeComputer(rv, pad_program=False)
        rv, code = computer.run_until_input_or_done()
        assert rv == []
        assert computer.program == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

    def test_addition(self):
        computer = IntCodeComputer([1, 0, 0, 0, 99], pad_program=False)
        rv, code = computer.run_until_input_or_done()
        assert computer.program == [2, 0, 0, 0, 99]

    def test_multiplication(self):
        computer = IntCodeComputer([2, 4, 4, 5, 99, 0], pad_program=False)
        rv, code = computer.run_until_input_or_done()
        assert computer.program == [2, 4, 4, 5, 99, 9801]

    def test_mix(self):
        computer = IntCodeComputer([1, 1, 1, 4, 99, 5, 6, 0, 99], pad_program=False)
        rv, code = computer.run_until_input_or_done()
        assert computer.program == [30, 1, 1, 4, 2, 5, 6, 0, 99]
