def ing_ly(string):
    if len(string) >= 3:
        return (string[:-3] + 'ly' if string.endswith('ing') else string + 'ing')

    return string
