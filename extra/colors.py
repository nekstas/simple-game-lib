from lib import *

def init(state: State, is_first_time: bool):
    state.board = generate_board(8, 8)
    return 'Шахматное поле'


def step(state: State) -> StepResult:
    return GAME_OVER


def draw(state: State):
    for x in range(state.board_width):
        for y in range(state.board_height):
            color = "#0f0"
            if (x + y) % 2 == 0:
                color = "#8a72e8"

            set_cell_color(state, Vec(x, y), color)


def on_key_press(state: State, key: Key):
    pass


start(init, step, draw, on_key_press, 1, 100)
