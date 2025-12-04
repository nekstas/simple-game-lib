import asyncio as _asyncio
import typing as _typing
from collections.abc import Coroutine as _Coroutine

import flet as _ft
import flet.canvas as _cv

import lib._types as _types
import lib._consts as _consts
import lib._state as _state
import lib._utils as _utils
import lib._asserts as _asserts

_TargetFunc = _typing.Callable[[_ft.Page], _Coroutine]
InitFunc = _typing.Callable[[_state.State, bool], str]
OnKeyPressFunc = _typing.Callable[[_state.State, _types.Key], None]
StepFunc = _typing.Callable[[_state.State], _types.StepResult]
DrawFunc = _typing.Callable[[_state.State], None]

REQUIRED_FIELDS = {'board'}


def _create_canvas(state: _state.State, cell_size: int) -> _cv.Canvas:
    return _cv.Canvas(
        width=state.board_width * cell_size,
        height=state.board_width * cell_size
    )


def _create_info_label() -> _ft.Text:
    return _ft.Text(
        size=24,
        text_align=_ft.TextAlign.CENTER,
    )


def _render_board(state: _state.State, cell_size: int, canvas: _cv.Canvas):
    last_row = state.board_height - 1
    canvas.shapes = [
        _cv.Rect(
            x * cell_size, (last_row - y) * cell_size,
            cell_size, cell_size,
            paint=_ft.Paint(style=_ft.PaintingStyle.FILL, color=state.board[x][y])
        )
        for x in range(state.board_width)
        for y in range(state.board_height)
    ]


def _render_all(
        draw_func: DrawFunc, state: _state.State, cell_size: int,
        info_label: _ft.Text, canvas: _cv.Canvas, page: _ft.Page
):
    draw_func(state)

    _render_board(state, cell_size, canvas)
    info_label.value = state.info_text

    page.update()


def _setup_page(page: _ft.Page, info_label: _ft.Text, canvas: _cv.Canvas):
    page.add(_ft.SafeArea(
        _ft.Row(
            [_ft.Column(
                [
                    _ft.Row(
                        [info_label],
                        alignment=_ft.MainAxisAlignment.CENTER,
                    ),
                    canvas
                ],
                alignment=_ft.MainAxisAlignment.CENTER,
            )],
            alignment=_ft.MainAxisAlignment.CENTER,
        ),
        expand=True
    ))


def _set_on_keyboard_event(state: _state.State, on_key_press_func: OnKeyPressFunc, page: _ft.Page):
    def _on_keyboard_event(event: _ft.KeyboardEvent):
        on_key_press_func(state, event.key)

    page.on_keyboard_event = _on_keyboard_event


def _create_start_state(init_func: InitFunc, page: _ft.Page) -> _state.State:
    state = _state.State()

    title = init_func(state, True)
    _asserts.assert_title(title)
    page.title = title

    initialized_fields = state.get_initialized_fields()
    assert initialized_fields == REQUIRED_FIELDS, \
        f'Поля {REQUIRED_FIELDS - initialized_fields} не были инициализированы.'
    return state


async def _restart_game(
        init_func: InitFunc, draw_func: DrawFunc,
        restart_delay: float, state: _state.State,
        info_label: _ft.Text, canvas: _cv.Canvas, page: _ft.Page
) -> int:
    await _asyncio.sleep(restart_delay)

    state.clear_initialized_fields()

    title = init_func(state, False)
    _asserts.assert_title(title)
    page.title = title

    cell_size = _utils.calculate_cell_size(state)
    _render_all(draw_func, state, cell_size, info_label, canvas, page)

    return cell_size


def _run_app(target: _TargetFunc):
    _ft.app(
        target,
        host='0.0.0.0',
        port=8080,
        view=_ft.AppView.FLET_APP_WEB
    )


def start(
        init_func: InitFunc, step_func: StepFunc, draw_func: DrawFunc,
        on_key_press_func: OnKeyPressFunc,
        steps_per_second: int, restart_delay: float
):
    _asserts.assert_steps_per_second(steps_per_second)
    steps_delay: float = 1 / steps_per_second

    async def main_target(page: _ft.Page):
        state = _create_start_state(init_func, page)

        cell_size = _utils.calculate_cell_size(state)
        info_label = _create_info_label()
        canvas = _create_canvas(state, cell_size)

        _setup_page(page, info_label, canvas)
        _set_on_keyboard_event(state, on_key_press_func, page)
        _render_all(draw_func, state, cell_size, info_label, canvas, page)

        while True:
            await _asyncio.sleep(steps_delay)
            step_result = step_func(state)
            _render_all(draw_func, state, cell_size, info_label, canvas, page)

            if step_result == _consts.GAME_OVER:
                cell_size = await _restart_game(
                    init_func, draw_func, restart_delay, state,
                    info_label, canvas, page
                )

    _run_app(main_target)
