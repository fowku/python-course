def remove_adjacent(input_list):
    if len(input_list) > 0:

        new_list = [input_list[0]]

        for element in input_list:
            if new_list[-1] == element:
                new_list.append(element)

        input_list = new_list

    return input_list


print(remove_adjacent([1, 2, 4, 4, 3, 3, 3, 5, 15, 15, 12, 2, 4, 4, 4, 4]))
