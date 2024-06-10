def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    counts = {}

    for num in mums:   # counts all the numbers in the list and how many times they occur as a value
        counts[num] = counts.get(num, 0) + 1

    max_value = max(counts.values()) # will return the num with the highest occurence

    for (num, freq) in counts.items():
        if freq == max_value:
            return num  # I don't understand the frequency argument.
    

