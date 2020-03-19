import functools


def trace_if(predicate):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if predicate(*args, **kwargs):
                print(func.__name__, args, kwargs)
            return func(*args, **kwargs)
        return inner
    return decorator


@trace_if(lambda x, y, **kwargs: kwargs.get("integral"))
def div(x, y, integral=False):
    return x // y if integral else x / y


div(4, 2)

div(4, 2, integral=True)
