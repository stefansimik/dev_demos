class MainClass(object):
    """This class docstring shows how to use sphinx and rst syntax."""

    @staticmethod
    def add_numbers(x, y):
        """This is function docstring, which can contain even Latex: :math:`a^2`

        :param x: the first value
        :param y: the second value
        :type x: int, float,...
        :type y: int, float,...
        :returns: sum of input numbers
        :rtype: int, float

        Example of code / literal block::

            import math
            from lib1 import function1
            from lib2 import function2

        Doctest example:

        >>> MainClass().add_numbers(1, 2)
        3
        """
        return x + y
