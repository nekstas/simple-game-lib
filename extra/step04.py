from lib import *


def get_center(state):
    return Vec(state.board_width, state.board_height) // 2


def get_initial_snake_pos(state):
    return get_center(state)


def init(state, is_first_time):
    state.board = generate_board(40, 30)
    state.data.snake = [get_initial_snake_pos(state)]
    return 'Змейка'


def step(state):
    pass


def draw(state):
    clear_board(state)

    for pos in state.data.snake:
        set_cell_color(state, pos, GREEN)


def on_key_press(state, key):
    pass


start(init, step, draw, on_key_press)
