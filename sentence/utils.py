# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


def enumerate_digits(number):
    """
    :type number: int or long
    :rtype: collections.Iterable[int, int]
    """
    position = 0
    while number > 0:
        digit = number % 10
        number //= 10
        yield position, digit
        position += 1