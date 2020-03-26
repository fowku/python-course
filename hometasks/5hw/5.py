def not_bad(string):
    not_ind = string.find('not')
    bad_ind = string.find('bad')

    if not_ind == -1 or bad_ind == -1:
        return string

    if not_ind < bad_ind:
        return string[:not_ind] + 'good' + string[bad_ind+3:]

    return string
