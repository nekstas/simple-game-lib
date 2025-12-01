from __future__ import annotations

import src.lib._limits as _limits
import src.lib._state as _state


def calculate_cell_size(state: _state.State):
    # TODO: может быть считать размеры относительно реального окна
    cell_width_size = _limits.Board.MAX_PIXELS_WIDTH // state.board_width
    cell_height_size = _limits.Board.MAX_PIXELS_HEIGHT // state.board_height
    return min(cell_width_size, cell_height_size)

