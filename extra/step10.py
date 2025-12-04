from lib import *

DIR_UP = Vec(0, 1)
DIR_DOWN = Vec(0, -1)
DIR_LEFT = Vec(-1, 0)
DIR_RIGHT = Vec(1, 0)


def is_opposite_direction(old_dir, new_dir):
    return old_dir == -new_dir


def snake_eats_apple(state: State) -> bool:
    return state.data.snake[-1] == state.data.apple


def get_center(state):
    return Vec(state.board_width, state.board_height) // 2


def get_initial_snake_pos(state):
    return get_center(state)


def get_empty_cells(state):
    snake_cells = set(state.data.snake)
    result = []

    for x in range(state.board_width):
        for y in range(state.board_height):
            pos = Vec(x, y)
            if pos not in snake_cells:
                result.append(pos)

    return result


def generate_apple(state):
    empty_cells = get_empty_cells(state)
    if not empty_cells:
        return None
    return rand_choice(empty_cells)


def update_best_score(state: State):
    score = len(state.data.snake)
    state.data.best_score = max(state.data.best_score, score)


def create_new_head(state):
    snake = state.data.snake
    state.data.dir = state.data.new_dir
    snake.append(snake[-1] + state.data.dir)
    snake[-1] %= state.board_size


def cut_the_snake(state):
    if state.data.extra_length > 0:
        state.data.extra_length -= 1
    else:
        state.data.snake.pop(0)


def init(state, is_first_time):
    if is_first_time:
        state.data.best_score = 0

    state.board = generate_board(40, 30)
    state.data.snake = [get_initial_snake_pos(state)]
    state.data.dir = DIR_RIGHT
    state.data.new_dir = DIR_RIGHT
    state.data.extra_length = 2
    state.data.apple = generate_apple(state)

    return 'Змейка'


def step(state):
    snake = state.data.snake
    create_new_head(state)

    if snake_eats_apple(state):
        state.data.extra_length += 1
        state.data.apple = generate_apple(state)

    cut_the_snake(state)

    update_best_score(state)
    state.info_text = f'Очки: {len(snake)}. Рекорд: {state.data.best_score}.'
    return GAME_CONTINUE


def draw(state):
    clear_board(state)

    for pos in state.data.snake:
        set_cell_color(state, pos, GREEN)
    set_cell_color(state, state.data.apple, RED)


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
