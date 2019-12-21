from src.input_helpers.read_intcode import parse_list_of_ints


def test_basic_parse():
    rv = parse_list_of_ints("../../inputData/day2test1")
    assert rv == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
