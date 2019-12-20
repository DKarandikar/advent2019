from src.day20 import get_shortest_distance_start_to_end


def test_day_20_small():
    rv = get_shortest_distance_start_to_end("../inputData/day20test1")
    assert rv == 23


def test_day_20_medium():
    rv = get_shortest_distance_start_to_end("../inputData/day20test2")
    assert rv == 58
