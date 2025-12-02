from lib import *

DIR_UP = Vec(0, 1)
DIR_DOWN = Vec(0, -1)
DIR_LEFT = Vec(-1, 0)
DIR_RIGHT = Vec(1, 0)


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


def init(state: State, is_first_time: bool):
    if is_first_time:
        state.data.best_score = 0

    state.board = generate_board(40, 30)
    center = Vec(state.board_width, state.board_height) // 2

    state.data.snake = [center]
    state.data.dir = DIR_RIGHT
    state.data.extra_length = 2
    state.data.apple = generate_apple(state)


def step(state: State) -> StepResult:
    snake: list[Vec] = state.data.snake

    snake.append(snake[-1] + state.data.dir)
    snake[-1] %= state.board_size

    if snake[-1] == state.data.apple:
        state.data.extra_length += 1
        state.data.apple = generate_apple(state)

        if state.data.apple is None:
            update_best_score(state)
            state.info_text = f'Вы победили! Очки: {len(snake)}'
            return GAME_OVER

    if state.data.extra_length > 0:
        state.data.extra_length -= 1
    else:
        snake.pop(0)

    if snake[-1] in snake[:-1]:
        state.info_text = f'Вы проиграли! Очки: {len(snake)}'
        return GAME_OVER

    update_best_score(state)
    state.info_text = f'Очки: {len(snake)}. Рекорд: {state.data.best_score}'
    return GAME_CONTINUE


def draw(state: State):
    clear_board(state)

    for pos in state.data.snake:
        set_cell_color(state, pos, GREEN)
    set_cell_color(state, state.data.apple, RED)


def on_key_press(state: State, key: Key):
    old_dir = state.data.dir

    if is_one_of_keys(key, {KEY_UP, KEY_W}):
        state.data.dir = DIR_UP
    if is_one_of_keys(key, {KEY_DOWN, KEY_S}):
        state.data.dir = DIR_DOWN
    if is_one_of_keys(key, {KEY_LEFT, KEY_A}):
        state.data.dir = DIR_LEFT
    if is_one_of_keys(key, {KEY_RIGHT, KEY_D}):
        state.data.dir = DIR_RIGHT

    # Восстанавливаем предыдущее направление, если мы повернули в противоположную сторону
    if state.data.dir == -old_dir:
        state.data.dir = old_dir


start(init, step, draw, on_key_press, 20, 5)
