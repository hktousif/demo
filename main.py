from __future__ import print_function
from fractions import Fraction
from functools import reduce

from pip._vendor.distlib.compat import raw_input


def product(fracs):
    t = reduce(lambda x, y: x * y, fracs, 1)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, raw_input().split())))
    print(fracs)
# print(*result)
