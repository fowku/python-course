def get_number_dict():
    dictionary = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten'
    }

    return dictionary


def ten_green_bottles():
    numbers_dict = get_number_dict()
    bottles = 10
    repeat = 0

    while bottles > 0:
        while repeat < 2:
            print(f'{numbers_dict[bottles]} green bottles sitting on the wall')
            repeat += 1
        repeat = 0

        print('And if one green bottle should accidentally fall,\nThere’ll be nine green bottles sitting on the wall.\n')

        bottles -= 1


ten_green_bottles()
