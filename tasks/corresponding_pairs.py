from typing import TypeVar

__all__ = ("corresponding_pairs",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def corresponding_pairs(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    """Формирует список пар из пары списков.

    Example:
        >> corresponding_pairs([1, 2], [3, 4])
        [(1, 3), (2, 4)]
    """
    result = []
    length = len(arr1)
    if len(arr2) < length:
        length = len(arr2)
    for i in range(length):
        result.append((arr1[i], arr2[i]))
    return result
