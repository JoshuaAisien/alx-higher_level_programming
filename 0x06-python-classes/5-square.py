"""define a square class"""


class Square:
    """Define square
    this class declares an argument size with checks if it is a positive int

    Attributes:
         size(int) : the size of square
         value(int): value to be set to size when called upon


    Methods:
        size: property value to set and the value of size
        Area: calculates the area of the square

    Example:
        #creating a square object
        square_1 = square(5)
        square_1.area()
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


    @property
    def size(self):
        """
        this is a getter to return the value of size when asked
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        this is property is used to set the size to value

        Args:
            value(int) the value to be to size

        Returns:
            __size(int): size of square
        """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")

        self.__size = value

    def area(self):
        """ defines the area of a square

        Returns:
         int: the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        print to stdout the square with the character '#'


        """
        if self.__size == 0:
            print()

        for i in range(self.__size + 1):
            for j in range(self.__size + 1):
                print("#", end="")
            print(" ")


