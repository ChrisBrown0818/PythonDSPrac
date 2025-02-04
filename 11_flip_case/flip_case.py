def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_sawp = to_swap.lower()
    out = ''

    for ltr in phrase:
        if ltr.lower() == to_sawp:
            ltr = ltr.swapcase()
        out += ltr
    return out
