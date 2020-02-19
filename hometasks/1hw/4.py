# функция, которая принимает один аргумент -- словарь
def invert_dict(old_dict):
    inverted_dict = {}

    for key, value in old_dict.items():
        for elem in value:
            inverted_dict.setdefault(elem, []).append(key)

    return inverted_dict
