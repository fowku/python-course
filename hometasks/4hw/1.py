import functools


def n_times(n=1):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return inner
    return decorator


@n_times(5)
def test(a, b, c):
    print('a')


test(12, '32', ['s', 'a'])
