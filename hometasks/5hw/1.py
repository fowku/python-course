from collections import defaultdict


def reverse_dict(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    original = defaultdict(list)

    # split into common dictionary
    for line in lines:
        word, translations = line.strip().split(' - ')
        original[word].extend(translations.split(', '))

    reversed_dict = defaultdict(list)

    # reverse dictionary
    for key, values in original.items():
        for elem in values:
            reversed_dict[elem].append(key)

    # sort values
    for key in reversed_dict:
        reversed_dict[key].sort()

    output = open('output.txt', 'w')

    # write to new file
    for word in sorted(reversed_dict):
        output.write(word + ' - ' + ', '.join(reversed_dict[word]) + '\n')

    output.close()
