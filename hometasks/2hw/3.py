from math import gcd


def lcm_two(a, b):
    return abs(a * b)//gcd(a, b)


def lcm(a, b, *numbers):
    prev_lcm = lcm_two(a, b)

    for i in range(len(numbers)):
        prev_lcm = lcm_two(prev_lcm, numbers[i])

    return prev_lcm
