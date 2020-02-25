def get_number_list():
    list = [
        'One',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
        'Eight',
        'Nine',
        'Ten'
    ]

    return list


def ten_green_bottles():
    numbers_dict = get_number_list()
    bottles = 9
    repeat = 0

    while bottles >= 0:
        while repeat < 2:
            print(f'{numbers_dict[bottles]} green bottles sitting on the wall')
            repeat += 1
        repeat = 0

        print('And if one green bottle should accidentally fall,\nThere’ll be nine green bottles sitting on the wall.\n')

        bottles -= 1


ten_green_bottles()
