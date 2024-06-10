def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    factors = []

    while(n <= num): # while  n less than or equal to num
        if n % num == 0: # if n modulus num = 0
            factors.append(n) # then add it to the factors list
        n += 1 # continue to next number

    return factors # return your new list

