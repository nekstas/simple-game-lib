from __future__ import annotations

import copy as _copy
import typing as _typing

import lib._types as _types
import lib._colors as _colors
import lib._vec as _vec


class StateData:
    _data: dict[str, _typing.Any]

    def __init__(self):
        super().__setattr__('_data', {})

    def __getattr__(self, key: str) -> _typing.Any:
        data = super().__getattribute__('_data')
        assert key in data, f'Аттрибут {key} не существует на момент обращения.'
        return data[key]

    def __setattr__(self, key: str, value: _typing.Any):
        data = super().__getattribute__('_data')
        data[key] = value

    def get_all(self) -> dict[str, _typing.Any]:
        return super().__getattribute__('_data')


class State:
    _info_text: str
    _board: _types.Board
    _initialized_fields: set[str]
    _data: StateData

    def __init__(self):
        self._initialized_fields = set()
        self._data = StateData()
        self._info_text = ''

    def __repr__(self) -> str:
        data_lines = [
            f'        {key}={repr(value)},'
            for key, value in self.data.get_all().items()
        ]

        return (f'{self.__class__.__name__}(\n'
                f'    info_text={repr(self.info_text)},\n'
                f'    board=Board(width={self.board_width}, height={self.board_height}, ...),\n'
                f'    data=Data(\n'
                f'{"\n".join(data_lines)}\n'
                f'    )\n'
                f')')

    @property
    def info_text(self) -> str:
        return self._info_text

    @info_text.setter
    def info_text(self, info_text: str):
        import lib._asserts as _asserts

        _asserts.assert_info_text(info_text)
        self._info_text = info_text

    @property
    def board(self) -> _types.Board:
        self._assert_initialized('board', 'Нельзя получить игровое поле')
        return self._board

    @board.setter
    def board(self, board: _types.Board):
        import lib._asserts as _asserts

        self._assert_not_initialized('board')

        assert isinstance(board, list), 'Поле должно быть списком списков цветов для каждой клетки.'
        width = len(board)
        _asserts.assert_width(width)

        assert isinstance(board[0], list), 'Поле должно быть списком списков цветов для каждой клетки.'
        height = len(board[0])
        _asserts.assert_height(height)

        for i, column in enumerate(board, 1):
            assert isinstance(column, list), 'Поле должно быть списком списков цветов для каждой клетки.'
            assert len(column) == height, \
                f'Высота {len(column)} столбца {i} отличается от высоты {height} первого столбца.'

        heights = [len(column) for column in board]
        assert min(heights) == max(heights), ('Высота некоторых столбцов различается. '
                                              f'Высоты: {heights}.')

        assert all(
            _colors.is_color(cell)
            for column in board
            for cell in column
        ), 'Все клетки поля должны быть заданы их цветом.'

        self._board = board
        self._initialized_fields.add('board')

    @property
    def board_width(self) -> int:
        self._assert_initialized('board', 'Нельзя получить ширину')
        return len(self._board)

    @board_width.setter
    def board_width(self, width: int) -> int:
        raise RuntimeError('Поле board_width нельзя изменять напрямую.')

    @property
    def board_height(self) -> int:
        self._assert_initialized('board', 'Нельзя получить высоту')
        return len(self._board[0])

    @board_height.setter
    def board_height(self, width: int) -> int:
        raise RuntimeError('Поле board_height нельзя изменять напрямую.')

    @property
    def board_size(self) -> _vec.Vec:
        return _vec.Vec(self.board_width, self.board_height)

    @board_size.setter
    def board_size(self, width: int) -> int:
        raise RuntimeError('Поле board_size нельзя изменять напрямую.')

    @property
    def data(self) -> StateData:
        return self._data

    @data.setter
    def data(self, data: StateData) -> int:
        raise RuntimeError('Полю `data` нельзя присваивать какое-либо значение.'
                           'Обращайтесь к его (любым) аттрибутам.')

    def _assert_initialized(self, attr: str, hint: str):
        assert attr in self._initialized_fields, f'{hint}, так как {attr} не инициализирован.'

    def _assert_not_initialized(self, attr: str):
        assert attr not in self._initialized_fields, f'Поле {attr} нельзя присваивать дважды.'

    def get_initialized_fields(self) -> set[str]:
        return _copy.copy(self._initialized_fields)

    def clear_initialized_fields(self):
        self._initialized_fields = set()
