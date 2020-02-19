def kollatz_hypothesis():
    number = int(input())
    result = [number]

    while number != 1:
        if number % 2 == 0:
            number /= 2
            result.append(number)
            continue

        number = 3*number + 1
        result.append(number)

    return result
