import numpy as np


def parse_text_grid_to_numpy_array(filename: str) -> np.array:
    rv = []
    lineLength = None
    with open(filename, "r") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            if lineLength and len(line) != lineLength:
                raise ValueError(f"Input grid has variable line lengths, line: {line}")
            else:
                lineLength = len(line)
            rv.append([char for char in line if char != "\n"])

    return np.array(rv).swapaxes(0, 1)
