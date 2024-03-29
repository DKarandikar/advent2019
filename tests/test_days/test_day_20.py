from src.day20 import get_shortest_distance_start_to_end, get_shortest_distance_start_to_end_layers
from src.input_helpers.input_path import get_input_file


def test_day_20_small():
    rv = get_shortest_distance_start_to_end(get_input_file("day20test1"))
    assert rv == 23


def test_day_20_medium():
    rv = get_shortest_distance_start_to_end(get_input_file("day20test2"))
    assert rv == 58


def test_day_20_small_layers():
    rv = get_shortest_distance_start_to_end_layers(get_input_file("day20test1"))
    assert rv == 26


def test_day_20_medium_layers():
    rv = get_shortest_distance_start_to_end_layers(get_input_file("day20test3"))
    assert rv == 396
