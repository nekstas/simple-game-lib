import typing as _typing

import lib._limits as _limits
import lib._colors as _colors
import lib._state as _state
import lib._vec as _vec


def _assert_board_size(value: _typing.Any, name: str, limit: int):
    assert isinstance(value, int), f'{name} поля должна быть целым числом (сейчас {type(value)})'
    assert value > 0, f'{name} поля должна быть положительной (сейчас {value}).'
    assert value <= _limits.Board.MAX_WIDTH, f'{name} поля должна быть не больше {limit} (сейчас {value})'


def assert_width(value: _typing.Any):
    _assert_board_size(value, 'Ширина', _limits.Board.MAX_WIDTH)


def assert_height(value: _typing.Any):
    _assert_board_size(value, 'Высота', _limits.Board.MAX_HEIGHT)


def assert_color(value: _typing.Any):
    assert _colors.is_color(value), f'Ожидался цвет, но было передано {value}.'


def assert_key_like(value: _typing.Any):
    assert isinstance(value, str), f'Ожидалось название клавиши на клавиатуре, но было передано {value}.'


def assert_vector_coord(value: _typing.Any):
    assert isinstance(value, int), f'Координаты точки/направления должны быть целыми (сейчас {value}).'


def assert_steps_per_second(value: _typing.Any):
    assert isinstance(value, int), 'Количество шагов в секунду должно быть целым числом.'
    assert value > 0, 'Количество шагов в секунду должно быть положительным.'
    assert value <= _limits.MAX_STEPS_PER_SECOND, (f'Количество шагов в секунду должно быть '
                                                   f'не больше {_limits.MAX_STEPS_PER_SECOND}')


def assert_state(value: _typing.Any):
    assert isinstance(value, _state.State), 'Ожидалось игровое состояние, получен объект {value}.'


def assert_vector(value: _typing.Any):
    assert isinstance(value, _vec.Vec), f'Ожидался объект класса Vec, получен объект {value}.'


def assert_vector_in_rect(value: _typing.Any, min_vector: _vec.Vec, max_vector: _vec.Vec):
    assert_vector(value)
    assert min_vector.x <= value.x <= max_vector.x, \
        f'Для координаты x неверно, что x = {value.x} лежит на отрезке [{min_vector.x}, {max_vector.x}]'
    assert min_vector.y <= value.y <= max_vector.y, \
        f'Для координаты y неверно, что y = {value.y} лежит на отрезке [{min_vector.y}, {max_vector.y}]'


def assert_vector_in_board(value: _typing.Any, state: _state.State):
    assert_vector_in_rect(
        value,
        _vec.Vec(0, 0),
        _vec.Vec(state.board_width - 1, state.board_height - 1)
    )


def assert_info_text(value: _typing.Any):
    assert isinstance(value, str), 'Выводимый текст должен быть строкой.'
    assert len(value) <= _limits.InfoText.MAX_LENGTH


def assert_title(value: _typing.Any):
    assert isinstance(value, str), 'Название приложения должно быть строкой.'
    assert len(value) <= _limits.Title.MAX_LENGTH