__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    result = 0
    even = None
    odd = None
    length = len(numbers)
    even = sum(numbers[i] for i in range(0, length) if i % 2 == 1)
    odd = sum(numbers[i] for i in range(0 ,length) if i % 2 == 0)

    if length >= 2:
        if odd != 0:
            result = even / odd


    print(f"{even} \ {odd} = {result}")
    return result

