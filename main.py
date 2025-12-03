from lib import *

DIR_UP = Vec(0, 1)
DIR_DOWN = Vec(0, -1)
DIR_LEFT = Vec(-1, 0)
DIR_RIGHT = Vec(1, 0)


def is_opposite_direction(old_dir, new_dir) -> bool:
    return old_dir == -new_dir


def snake_eats_apple(state: State) -> bool:
    return state.data.snake[-1] == state.data.apple


def is_win(state: State) -> bool:
    return state.data.apple is None


def is_lose(state: State) -> bool:
    snake = state.data.snake
    return snake[-1] in snake[:-1]


def get_center(state: State) -> Vec:
    return Vec(state.board_width, state.board_height) // 2


def get_initial_snake_pos(state: State) -> Vec:
    return get_center(state)


def get_empty_cells(state: State) -> list[Vec]:
    snake_cells = set(state.data.snake)
    result = []

    for x in range(state.board_width):
        for y in range(state.board_height):
            pos = Vec(x, y)
            if pos not in snake_cells:
                result.append(pos)

    return result


def generate_apple(state: State) -> Vec | None:
    empty_cells = get_empty_cells(state)
    if not empty_cells:
        return None
    return rand_choice(get_empty_cells(state))


def update_best_score(state: State):
    score = len(state.data.snake)
    state.data.best_score = max(state.data.best_score, score)


def create_new_head(state: State):
    snake = state.data.snake
    state.data.dir = state.data.new_dir
    snake.append(snake[-1] + state.data.dir)
    snake[-1] %= state.board_size


def cut_the_snake(state: State):
    if state.data.extra_length > 0:
        state.data.extra_length -= 1
    else:
        state.data.snake.pop(0)


def init(state: State, is_first_time: bool):
    if is_first_time:
        state.data.best_score = 0

    state.board = generate_board(40, 30)

    state.data.snake = [get_initial_snake_pos(state)]
    state.data.dir = DIR_RIGHT
    state.data.new_dir = DIR_RIGHT
    state.data.extra_length = 2
    state.data.apple = generate_apple(state)


def step(state: State) -> StepResult:
    snake: list[Vec] = state.data.snake

    create_new_head(state)

    if snake_eats_apple(state):
        state.data.extra_length += 1
        state.data.apple = generate_apple(state)

    if is_win(state):
        update_best_score(state)
        state.info_text = f'Вы победили! Очки: {len(snake)}'
        return GAME_OVER

    cut_the_snake(state)

    if is_lose(state):
        state.info_text = f'Вы проиграли! Очки: {len(snake)}'
        return GAME_OVER

    update_best_score(state)
    state.info_text = f'Очки: {len(snake)}. Рекорд: {state.data.best_score}.'
    return GAME_CONTINUE


def draw(state: State):
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


start(init, step, draw, on_key_press, 20, 5)
