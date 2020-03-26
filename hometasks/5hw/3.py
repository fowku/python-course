def pi_entry():
    number = input('Enter sequence to search for')
    file = open('pi.txt', 'r')
    pi = file.readlines()
    file.close()

    entries = []

    if number == '3':
        entries.append(0)

    length_of_str = len(pi[1])

    for i in range(1, len(pi)):
        entry = pi[i].find(number)

        if entry > -1:
            entries.append(length_of_str * (i - 1) + entry + 3)

    print('Found ', len(entries), ' results')

    if len(entries) > 5:
        print('Positions:', entries[0:5], '...')
    else:
        print('Positions:', entries)
