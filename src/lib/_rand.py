import random as _random
import typing as _typing


def rand_int(min_number: int, max_number: int) -> int:
    assert isinstance(min_number, int), f'min_number должен быть числом, сейчас {min_number=}.'
    assert isinstance(max_number, int), f'min_number должен быть числом, сейчас {max_number=}.'
    assert min_number <= max_number, \
        f'min_number должен быть не больше max_number, сейчас {min_number=}, {max_number=}'
    return _random.randint(min_number, max_number)


def rand_index(size: int) -> int:
    assert isinstance(size, int), f'size должен быть числом, сейчас {size=}.'
    assert size > 0, f'Нельзя выбрать индекс, если длина последовательности {size} равна 0 (или отрицательная).'
    return rand_int(0, size - 1)


def rand_choice(elements: _typing.Collection) -> _typing.Any:
    try:
        sequence_list = list(elements)
        assert sequence_list, 'Последовательность для выбора элемента должна быть непустой.'
        return sequence_list[rand_index(len(elements))]
    except Exception:
        raise RuntimeError(
            'Для выбора случайного элемента из последовательности, '
            'последовательность должна уметь преобразовываться в список.'
        )
