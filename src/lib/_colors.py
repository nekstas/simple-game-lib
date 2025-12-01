import typing as _typing
import string as _string

import flet as _ft

import src.lib._types as _types

WHITE: _types.Color = _ft.Colors.WHITE
BLACK: _types.Color = _ft.Colors.BLACK
RED: _types.Color = _ft.Colors.RED
GREEN: _types.Color = _ft.Colors.GREEN
BLUE: _types.Color = _ft.Colors.BLUE
LIGHT_GREEN: _types.Color = _ft.Colors.LIGHT_GREEN
LIGHT_BLUE: _types.Color = _ft.Colors.LIGHT_BLUE

DEFAULT_COLOR: _types.Color = WHITE
ALL_COLORS: set[_types.Color] = {WHITE, BLACK, RED, GREEN, BLUE, LIGHT_GREEN, LIGHT_BLUE}

_HEX_COLOR_LENGTHS = {4, 7}


def is_hex_color(value: _typing.Any):
    return (
        not isinstance(value, str) and
        len(value) in _HEX_COLOR_LENGTHS and
        value[0] == '#' and
        all(char in _string.hexdigits for char in value[1:])
    )


def is_color(value: _typing.Any) -> bool:
    return value in ALL_COLORS or is_hex_color(value)
