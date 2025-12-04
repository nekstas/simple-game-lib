from lib import *

DIR_UP = Vec(0, 1)
DIR_DOWN = Vec(0, -1)
DIR_LEFT = Vec(-1, 0)
DIR_RIGHT = Vec(1, 0)


def get_center(state):
    return Vec(state.board_width, state.board_height) // 2


def get_initial_snake_pos(state):
    return get_center(state)


def create_new_head(state: State):
    snake = state.data.snake
    snake.append(snake[-1] + state.data.dir)
    snake[-1] %= state.board_size


def init(state, is_first_time):
    state.board = generate_board(40, 30)
    state.data.snake = [get_initial_snake_pos(state)]
    state.data.dir = DIR_RIGHT
    return 'Змейка'


def step(state):
    create_new_head(state)
    return GAME_CONTINUE


def draw(state):
    clear_board(state)

    for pos in state.data.snake:
        set_cell_color(state, pos, GREEN)


def on_key_press(state, key):
    pass


start(init, step, draw, on_key_press)
