import copy
from enum import Enum, auto
from typing import List, Tuple, Callable


class ReturnCode(Enum):
    finished = auto()
    need_input = auto()


OPLengths = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 3,
    7: 3,
    8: 3,
    9: 1,
}


class IntCodeComputer:
    def __init__(self, program: List[int], pad_program=True):
        self.index = 0
        self.relative_base = 0
        self.program = copy.deepcopy(program)
        self.rv = []
        self.input = []

        self.current_input = None
        self.modes = None

        if pad_program:
            self.pad_program()

        self.OPS = {
            x: getattr(self, f"do_op_{x}") for x in range(1, 3)
        }

    def pad_program(self):
        for _ in range(50000):
            self.program.append(0)

    def run_until_input_or_done(self) -> Tuple[List[int], ReturnCode]:
        input_ticker = 0
        while self.index < len(self.program):
            op, self.modes = self.get_op_code_and_parameters(self.program[self.index])
            if op == 99:
                return self.rv, ReturnCode.finished
            else:
                if op == 3:
                    try:
                        self.current_input = self.input[input_ticker]
                    except IndexError:
                        return self.rv, ReturnCode.need_input
                    input_ticker += 1

                self.OPS.get(op)()

    @staticmethod
    def get_op_code_and_parameters(operation: int) -> Tuple[int, List[int]]:
        if operation == 99:
            return 99, []
        operation = str(operation)

        if len(operation) >= 2:
            opcode = int(operation[-2:])
        else:
            opcode = int(operation)

        modes = []
        x = 3
        while True:
            try:
                modes.append(operation[-x])
                x += 1
            except IndexError:
                break

        while len(modes) < OPLengths.get(opcode):
            modes.append(0)

        return opcode, [int(p) for p in modes]

    def get_parameter_indices(self) -> List[int]:
        rv = []
        for i, mode in enumerate(self.modes):
            if mode == 0:
                rv.append(self.program[self.index + 1 + i])
            elif mode == 1:
                rv.append(self.program[self.index + 1 + i] + self.relative_base)
            elif mode == 2:
                rv.append(self.index + 1 + i)
            else:
                raise RuntimeError(f"Invalid mode: {mode}")
        return rv

    def _do_function_op(self, fn: Callable[[int, int], int]) -> None:
        indices = self.get_parameter_indices()

        self.program[indices[2]] = fn(
            self.program[indices[0]],
            self.program[indices[1]],
        )

        self.index += 4

    def do_op_1(self):
        self._do_function_op(lambda a, b: a + b)

    def do_op_2(self):
        self._do_function_op(lambda a, b: a * b)
