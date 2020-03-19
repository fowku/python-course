import functools


def checked(*types):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if len(types) == len(args):
                for i in range(len(types)):
                    if type(args[i]) != types[i]:
                        raise TypeError('Wrong type!')
            else:
                raise Exception('Wrong number of types!')
            return func(*args, **kwargs)
        return inner
    return decorator


@checked(int, int, float)
def do_sum_and_div(a, b, c):
    return c / (a + b)


print(do_sum_and_div(1, 2, 3.4))
