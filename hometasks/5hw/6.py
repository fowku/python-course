def nl(file_name=None):
    if not file_name:
        file_name = input('Enter file path: ')

    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    for line in range(len(lines)):
        number = str(line+1)
        _line = lines[line][:-1]
        print(number.rjust(len(number)+4) + _line.rjust(len(_line)+2))


nl('output.txt')
