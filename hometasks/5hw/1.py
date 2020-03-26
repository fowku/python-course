from collections import defaultdict


def reverse_dict(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    original = defaultdict(list, **{})

    # split into common dictionary
    for line in lines:
        words = line.strip().split(' - ')
        for word in words[1].split(', '):
            original[words[0]].append(word)

    reversed = defaultdict(list, **{})

    # reverse dictionary
    for key, values in original.items():
        for elem in values:
            reversed[elem].append(key)

    # sort values
    for key in reversed:
        reversed[key].sort()

    output = open('output.txt', 'w')

    # write to new file
    for word in sorted(reversed):
        output.write(word + ' - ' + ', '.join(reversed[word]) + '\n')

    output.close()
