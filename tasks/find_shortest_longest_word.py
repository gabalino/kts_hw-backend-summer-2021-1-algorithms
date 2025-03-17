import re

__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text
        содержит слова, (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """
    shortest_word = None
    longest_word = None

    words = re.findall(r"\w+", text)
    words.sort(key=len)
    if len(words) > 0:
        shortest_word = words[0]
        longest_word = words[-1]

    result = (shortest_word, longest_word)
    return result
