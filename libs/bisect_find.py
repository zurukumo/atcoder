import bisect


def find_lt(a: list[int], x: int):
    i = bisect.bisect_left(a, x)
    if i:
        return a[i - 1]
    return None


def find_le(a: list[int], x: int):
    i = bisect.bisect_right(a, x)
    if i:
        return a[i - 1]
    return None


def find_gt(a: list[int], x: int):
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    return None


def find_ge(a: list[int], x: int):
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    return None
