class CartesianProduct:
    def __init__(self, user_set, power, start=0):
        self._set = user_set
        self._power = power
        self._counter = start
        self._mod_number = len(user_set)**power

    def next(self):
        return CartesianProduct(self._set, self._power, self._counter + 1)

    def __str__(self):
        result_in_numbers = self._to_number_system(self._counter %
                                                   self._mod_number, len(self._set))

        to_print = self._get_in_symbols(result_in_numbers)

        return ', '.join(map(str, to_print))

    def _get_in_symbols(self, numbers):
        result = []

        if self._power > len(numbers):
            numbers = self._pad_list(numbers, self._power)

        for number in numbers:
            result.append(self._set[number])

        return result

    def _pad_list(self, list_to_add, pad):
        zeros_to_add = pad - len(list_to_add)
        pad_list = [0] * zeros_to_add

        return pad_list + list_to_add

    def _to_number_system(self, number, system):
        result = []

        if number == 0:
            return [0]

        while number >= system - 1:
            result.append(number % system)
            number //= system

        if number > 0:
            result.append(number)

        result.reverse()

        return result


cur = CartesianProduct([1, 'a', 'b'], 3)

for i in range(30):
    print(cur)
    cur = cur.next()
