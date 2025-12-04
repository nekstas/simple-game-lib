from lib import *


def init(state, is_first_time):
    state.board = generate_board(40, 30)
    return 'Змейка'


def step(state):
    pass


def draw(state):
    pass


def on_key_press(state, key):
    pass


start(init, step, draw, on_key_press)
