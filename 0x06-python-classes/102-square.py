class Square:
    """
    this is a first class task.
    this class doesnt do anything.
    @size is a private attribute.
    @area is a method that calculates the area.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        if val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    def area(self):
        return (self.__size * self.__size)

    def __eq__(self, another):
        return self.area() == another.area()

    def __ne__(self, another):
        return self.area() != another.area()

    def __lt__(self, another):
        return self.area() < another.area()

    def __le__(self, another):
        return self.area() <= another.area()

    def __gr__(self, another):
        return self.area() > another.area()

    def __gr__(self, another):
        return self.area() >= another.area()
