def digits(number):
    if (number < 0):
        return []

    if number == 0:
        return [0]

    list_of_nums = []

    while number:
        list_of_nums.append(number % 10)
        number //= 10

    list_of_nums.reverse()

    return list_of_nums


print(digits(1914))
