import lib._types as _types
import lib._state as _state
import lib._vec as _vec
import lib._asserts as _asserts


def generate_board(width: int, height: int, color: _types.Color) -> _types.Board:
    _asserts.assert_width(width)
    _asserts.assert_height(height)
    _asserts.assert_color(color)

    board = []
    for x in range(width):
        board.append([])
        for y in range(height):
            board[x].append(color)
    return board


def is_one_of_keys(pressed_key: _types.Key, accepted_keys: set[_types.Key]) -> bool:
    _asserts.assert_key_like(pressed_key)
    return pressed_key in accepted_keys


def set_cell_color(state: _state.State, pos: _vec.Vec, color: _types.Color):
    _asserts.assert_vector_in_board(pos, state)
    state.board[pos.x][pos.y] = color


def get_cell_color(state: _state.State, pos: _vec.Vec) -> _types.Color:
    _asserts.assert_vector_in_board(pos, state)
    return state.board[pos.x][pos.y]


def clear_board(state: _state.State, color: _types.Color):
    _asserts.assert_color(color)
    for x in range(state.board_width):
        for y in range(state.board_height):
            set_cell_color(state, _vec.Vec(x, y), color)
