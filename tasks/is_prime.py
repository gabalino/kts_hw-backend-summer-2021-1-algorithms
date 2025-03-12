__all__ = ("is_prime",)

import math

def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    result = False
    if number > 2:
        square_root = int(math.sqrt(number))
        count = 0
        for i in range(2, square_root+1):
            if number % i == 0:
                count += 1
                if count > 1:
                    break
        if count == 0:
            result = True
    elif number == 2:
        result = True
    return result
