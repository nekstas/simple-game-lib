import typing as _typing

import lib._vec as _vec
import lib._state as _state
import lib._rand as _rand
import lib._impl as _impl
import lib._flet_impl as _flet_impl

from lib._colors import (
    WHITE,
    BLACK,
    RED,
    GREEN,
    BLUE,
    DEFAULT_COLOR,
)
from lib._keys import (
    KEY_UP,
    KEY_DOWN,
    KEY_LEFT,
    KEY_RIGHT,
    KEY_W,
    KEY_A,
    KEY_S,
    KEY_D
)
from lib._consts import (
    GAME_CONTINUE,
    GAME_OVER
)

# Различные используемые типы
Color = str
Key = str
StepResult = bool
Board = list[list[Color]]

# Различные сигнатуры функций
InitFunc = _typing.Callable[[_state.State, bool], None]
OnKeyPressFunc = _typing.Callable[[_state.State, Key], None]
StepFunc = _typing.Callable[[_state.State], StepResult]
DrawFunc = _typing.Callable[[_state.State], None]


class Vec(_vec.Vec):
    x: int
    y: int

    # Можно выполнять операции
    # Поэлементно: +, -, %
    # Унарные: +, -
    # Со скаляром: *, /
    # Сравнивать на равенство


class State(_state.State):
    board: Board
    info_text: str

    board_width: int  # Только для чтения
    board_height: int  # Только для чтения
    board_size: Vec  # Только для чтения

    # Можно работать с любыми аттрибутами этого объекта как с переменными
    # Например, data.score = 1, print(data.score)  # -> 1
    # При этом самому data ничего присваивать нельзя.
    data: _state.StateData


def rand_int(min_number: int, max_number: int) -> int:
    """
    Равновероятно возвращает случайное число от `min_number` до `max_number` включительно.
    """
    return _rand.rand_int(min_number, max_number)


def rand_index(size: int) -> int:
    """
    Равновероятно возвращает случайный индекс для коллекции размера `size`
    (число от `0` до `size - 1` включительно)
    """
    return _rand.rand_index(size)


def rand_choice(elements: _typing.Collection) -> _typing.Any:
    """
    Равновероятно выбирает случайный элемент переданной коллекции.
    """
    return _rand.rand_choice(elements)


def generate_board(
        width: int,
        height: int,
        color: Color = DEFAULT_COLOR
) -> Board:
    """
    Генерирует поле с шириной `width`, высотой `height`, заполненное цветом `color`
    (по умолчанию используется стандартный цвет)
    """
    return _impl.generate_board(width, height, color)


def is_one_of_keys(pressed_key: Key, accepted_keys: set[Key]) -> bool:
    """
    Проверяет, является ли нажатая клавиша `pressed_key`
    одной из ожидаемых клавиш `accepted_keys`.
    """
    return _impl.is_one_of_keys(pressed_key, accepted_keys)


def set_cell_color(
        state: State,
        pos: Vec,
        color: Color
):
    """
    Закрашивает клетку с координатами `pos.x` и `pos.y` в цвет `color`.
    """
    _impl.set_cell_color(state, pos, color)


def get_cell_color(
        state: State,
        pos: Vec
) -> Color:
    """
    Возвращает цвет клетки с координатами `pos.x` и `pos.y`
    """
    return _impl.get_cell_color(state, pos)


def clear_board(
        state: State,
        color: Color = DEFAULT_COLOR
):
    """
    Очищает всё поле, закрашивая его в цвет `color` (по умолчанию, белый)
    """
    return _impl.clear_board(state, color)


def start(
        init_func: _flet_impl.InitFunc,
        step_func: _flet_impl.StepFunc,
        draw_func: _flet_impl.DrawFunc,
        on_key_press_func: _flet_impl.OnKeyPressFunc,
        steps_per_second: int,
        restart_delay: float
):
    """
    Запускает игру с переданными функциями, выполняющими соответствующие действия.
    :param init_func: Функция, инициализирующая изначальное состояние.
    :param step_func: Функция, выполняющая один игровой шаг.
    :param draw_func: Функция, отображающая игровое состояние на игровое поле.
    :param on_key_press_func: Функция, обрабатывающая нажатие клавиш.
    :param steps_per_second: Примерное число шагов (кадров) в секунду.
    :param restart_delay: Количество секунд, спустя которое игра будет перезапущена после.
    """
    _flet_impl.start(
        init_func, step_func, draw_func,
        on_key_press_func,
        steps_per_second, restart_delay
    )
