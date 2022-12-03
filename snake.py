from enum import Enum


class Direction(Enum):
    """ Enum for the direction of the snake
        :param Enum: Enum class
        :return None:
    """

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    """ Snake class
        :param None:
        :return None:
    """

    def __init__(self, x, y, size, color) -> None:
        """ Constructor for the snake class 
            :param x: x
            :param y: y
            :param size: size
            :param color: color
            :return None:
        """

        self.length = None
        self.direction = None
        self.body = None

        self.block_size = None
        self.color = (0, 0, 255)
        self.bounds = None

        self.respawn()

    def respawn(self) -> None:
        """ Respawn the snake
            :param None:
            :return None:
        """

        self.length = 1
        self.direction = Direction.RIGHT
        self.body = [(0, 0)]
        self.block_size = 20
        self.color = (0, 0, 255)
        self.bounds = (800, 600)
