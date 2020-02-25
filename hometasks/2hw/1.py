def union(*sets):
    common_set = set()

    for _set in sets:
        common_set = common_set.union(_set)

    return common_set
