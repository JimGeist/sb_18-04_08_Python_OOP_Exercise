"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    'start', integer, initializes the generator to a starting number. 
        An error is raised when start is not an integer that is greater than 0.
    ValueError: start serial number must be greater than 0.
    ValueError: start 'one' is not an integer.

    generate() returns an integer which is the next available serial number

    reset() resets the serial number back to the initializing number

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    >>> serial = SerialGenerator(0)
    Traceback (most recent call last):
        ...
    ValueError: start serial number must be greater than 0.

    >>> serial = SerialGenerator("one")
    Traceback (most recent call last):
        ...
    ValueError: start 'one' is not an integer.

    """

    def __init__(self, start):
        """ Initialize serial number generator

        Errors are raised when start is not an integer or 
        when start is an integer that is not greater than 0

        """

        # start must be an integer that is greater than 0
        if (isinstance(start, int)):
            if (start > 0):
                self.start = start
                # self.next_serial is set by calling reset.
                # We only need to change the reset code in one place
                self.next_serial = None
                self.reset()
            else:
                raise ValueError(
                    f"start serial number must be greater than 0.")
        else:
            raise ValueError(f"start '{start}' is not an integer.")

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next_serial + 1}>"

    def generate(self):
        self.next_serial = self.next_serial + 1
        return self.next_serial

    def reset(self):
        self.next_serial = self.start - 1
