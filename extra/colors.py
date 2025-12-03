from lib import *

def init(state: State, is_first_time: bool):
    state.board = generate_board(8, 8)
    return 'Различные цвета'


def step(state: State) -> StepResult:
    return GAME_OVER


def draw(state: State):
    for x in range(state.board_width):
        for y in range(state.board_height):
            color = rand_choice([
                '#ff0000', '#00ff00', '#0000ff',
                '#ffff00', '#00ffff', '#ff00ff',
                '#ffffff', '#000000'
            ])
            set_cell_color(state, Vec(x, y), color)


def on_key_press(state: State, key: Key):
    pass


start(init, step, draw, on_key_press, 1, 5)
