"""Module contains basic movement tools"""

import pygame
from utils import CONFIG
from utils.timer import Time


class Movement:
    """Contains basic movement tools"""

    _grid_div = CONFIG.get("grid").get("min_div")
    _screen_width, screen_height = CONFIG.get("window").get("size")
    _ceil_size = _screen_width // _grid_div

    direction = [0, 0]
    next_position = [0, 0]

    @staticmethod
    def move(element: object, x: int, y: int):
        """"""
        if not Movement.direction[0]:
            Movement.direction[0] = x
            Movement.next_position[0] = Movement._ceil_size * x + element.rect.x

        if not Movement.direction[1]:
            Movement.direction[1] = y
            Movement.next_position[1] = Movement._ceil_size * y + element.rect.y

    @staticmethod
    def grid_move(element: object, speed: float = 2):
        """Returns the position in a grid of the next movement"""
        element.rect.x += (
            Movement._ceil_size * speed * Movement.direction[0] * Time.delta_time
        )
        element.rect.y += (
            Movement._ceil_size * speed * Movement.direction[1] * Time.delta_time
        )

        if element.rect.x >= Movement.next_position[0] and Movement.direction[0] == 1:
            Movement.direction[0] = 0
            element.rect.x = Movement.next_position[0]

        if element.rect.x <= Movement.next_position[0] and Movement.direction[0] == -1:
            Movement.direction[0] = 0
            element.rect.x = Movement.next_position[0]

        if element.rect.y >= Movement.next_position[1] and Movement.direction[1] == 1:
            Movement.direction[1] = 0
            element.rect.y = Movement.next_position[1]

        if element.rect.y <= Movement.next_position[1] and Movement.direction[1] == -1:
            Movement.direction[1] = 0
            element.rect.y = Movement.next_position[1]
