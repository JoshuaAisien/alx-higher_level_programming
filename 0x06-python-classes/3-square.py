"""define a square class"""


class Square:
    """Define square
    this class declares an argument size with checks if it is a positive int
    """

    def __init__(self, size=0):
        """initialize a  new square
        Args:
            size(int): size of the square(default 0).

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0 (negative)

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ defines the area of a square
        returns the area of a square
        """
        return self.__size * self.__size
