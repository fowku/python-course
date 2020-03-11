class Vector:
    def __init__(self, *coords):
        self._coordinates = list(coords)

    def __len__(self):
        return len(self._get_coords())

    def __add__(self, vector):
        self._check_type(vector)
        self._compare_lengths(vector)

        self_coords = self._get_coords()
        vector_coodrs = vector._get_coords()

        new_coords = []
        for self_elem, vector_elem in zip(self_coords, vector_coodrs):
            new_coords.append(self_elem + vector_elem)

        return Vector(*new_coords)

    def __sub__(self, vector):
        self._check_type(vector)
        self._compare_lengths(vector)

        self_coords = self._get_coords()
        vector_coodrs = vector._get_coords()

        new_coords = []
        for self_elem, vector_elem in zip(self_coords, vector_coodrs):
            new_coords.append(self_elem - vector_elem)

        return Vector(*new_coords)

    def __mul__(self, const):
        if not isinstance(const, int) and not isinstance(const, float):
            raise TypeError('Argument type is not a number')

        self_coords = self._get_coords()

        new_coords = []
        for self_elem in self_coords:
            new_coords.append(self_elem * const)

        return Vector(*new_coords)

    def dot(self, vector):
        self._check_type(vector)
        self._compare_lengths(vector)

        self_coords = self._get_coords()
        vector_coodrs = vector._get_coords()

        return sum([self_elem * vector_elem for self_elem,
                    vector_elem in zip(self_coords, vector_coodrs)])

    def __eq__(self, vector):
        if not isinstance(vector, Vector):
            return False

        self_coords = self._get_coords()
        vector_coodrs = vector._get_coords()

        if len(self) != len(vector):
            return False

        for self_elem, vector_elem in zip(self_coords, vector_coodrs):
            if self_elem != vector_elem:  # по хорошему float нужно сравнивать по модулю
                return False

        return True

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Index type is not an int')

        if index >= len(self):
            raise ValueError('Out of range')

        return self._get_coords()[index]

    def __str__(self):
        return ' '.join(map(str, self._get_coords()))

    def _get_coords(self):
        return self._coordinates

    def _check_type(self, arg):
        if not isinstance(arg, Vector):
            raise TypeError('Argument type is not Vector')

    def _compare_lengths(self, vector):
        if len(self) != len(vector):
            raise TypeError('Vectors have different lengths')


a = Vector(2, 32, 21.32, 32)
b = Vector(52, 23, 12.55, 87)
c = Vector(2, 32, 21.32, 32)

print(str(a + b))
print(str(a - b))
print(str(a * 4))
print(a.dot(b))
print(a == b)
print(a == c)
print(b[3])
