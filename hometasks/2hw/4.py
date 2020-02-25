def compose(*funcs):
    def res(num):
        for func in reversed(funcs):
            num = func(num)
        return num

    return res
