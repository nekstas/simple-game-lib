from lib import *

DIR_UP = Vec(0, 1)
DIR_DOWN = Vec(0, -1)
DIR_LEFT = Vec(-1, 0)
DIR_RIGHT = Vec(1, 0)


def is_opposite_direction(old_dir, new_dir):
    return old_dir == -new_dir


def get_center(state):
    return Vec(state.board_width, state.board_height) // 2


def get_initial_snake_pos(state):
    return get_center(state)


def create_new_head(state):
    snake = state.data.snake
    state.data.dir = state.data.new_dir
    snake.append(snake[-1] + state.data.dir)
    snake[-1] %= state.board_size


def init(state, is_first_time):
    state.board = generate_board(40, 30)
    state.data.snake = [get_initial_snake_pos(state)]
    state.data.dir = DIR_RIGHT
    state.data.new_dir = DIR_RIGHT
    return 'Змейка'


def step(state):
    create_new_head(state)
    return GAME_CONTINUE


def draw(state):
    clear_board(state)

    for pos in state.data.snake:
        set_cell_color(state, pos, GREEN)


def on_key_press(state: State, key: Key):
    if is_one_of_keys(key, {KEY_UP, KEY_W}):
        state.data.new_dir = DIR_UP
    if is_one_of_keys(key, {KEY_DOWN, KEY_S}):
        state.data.new_dir = DIR_DOWN
    if is_one_of_keys(key, {KEY_LEFT, KEY_A}):
        state.data.new_dir = DIR_LEFT
    if is_one_of_keys(key, {KEY_RIGHT, KEY_D}):
        state.data.new_dir = DIR_RIGHT

    if is_opposite_direction(state.data.new_dir, state.data.dir):
        state.data.new_dir = state.data.dir


start(init, step, draw, on_key_press)
