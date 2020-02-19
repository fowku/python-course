def merge_lists(lst1, lst2):
    new_list = []

    lst1_ind = 0
    lst2_ind = 0

    while lst1_ind < (len(lst1)) and lst2_ind < (len(lst2)):
        if lst1[lst1_ind] == lst2[lst2_ind]:
            new_list.append(lst1[lst1_ind])
            new_list.append(lst2[lst2_ind])
            lst1_ind += 1
            lst2_ind += 1
            continue

        if lst1[lst1_ind] < lst2[lst2_ind]:
            new_list.append(lst1[lst1_ind])
            lst1_ind += 1
            continue

        if lst2[lst2_ind] < lst1[lst1_ind]:
            new_list.append(lst2[lst2_ind])
            lst2_ind += 1
            continue

    if lst1_ind == len(lst1):
        new_list.extend(lst2[lst2_ind:])
    else:
        new_list.extend(lst1[lst1_ind:])

    return new_list


print(merge_lists([1, 2, 5, 10, 15], [1, 3, 7]))
