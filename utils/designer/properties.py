"""Contains properties for different elements"""

import pygame
from utils import CONFIG


class Rectangle:
    """Define a pygame rect"""

    @staticmethod
    def create_rect(position: tuple, size: tuple, unit: str) -> pygame.Rect:
        """Init a new rectangle object"""
        if unit == "pixel":
            rect = pygame.Rect(*position, *size)
        else:
            rect = pygame.Rect(Rectangle.calc_grid(position, size))

        return rect

    @staticmethod
    def calc_grid(position: list, size: list) -> tuple:
        """Calculate the position/size accourding to the grid config"""
        grid_div = CONFIG.get("grid").get("min_div")
        screen_width, screen_height = pygame.display.get_window_size()

        ceil_size = screen_width // grid_div

        return (
            ceil_size * position[0],
            ceil_size * position[1],
            ceil_size * size[0],
            ceil_size * size[1],
        )


class Text:
    """Define a pygame text"""

    def __init__(
        self,
        rect: pygame.Rect,
        text: str = "",
        antialias: bool = False,
        color: str = "black",
        alignment: str = "topleft",
        size: int = 16,
        font: str = None,
    ) -> None:
        """"""
        self._font = pygame.Font(font, size)
        self._rect = rect

        self.text = text
        self.antialias = antialias
        self.color = color

        self.font_obj = self.render_font()

        self.alignment = alignment
        self.x_offset, self.y_offset = self.set_alignment()

    def render_font(self) -> None:
        """"""
        return self._font.render(self.text, self.antialias, self.color)

    def set_alignment(self) -> tuple:
        """"""
        center_x = self._rect.width // 2 - self.font_obj.get_width() // 2
        right_x = self._rect.width - self.font_obj.get_width()

        center_y = self._rect.height // 2 - self.font_obj.get_height() // 2
        down_y = self._rect.height - self.font_obj.get_height()

        if self.alignment == "topleft":
            return (0, 0)
        if self.alignment == "midtop":
            return (center_x, 0)
        if self.alignment == "topright":
            return (right_x, 0)

        if self.alignment == "midleft":
            return (0, center_y)
        if self.alignment == "center":
            return (center_x, center_y)
        if self.alignment == "midright":
            return (right_x, center_y)

        if self.alignment == "bottomleft":
            return (0, down_y)
        if self.alignment == "midbottom":
            return (center_x, down_y)
        if self.alignment == "bottomright":
            return (right_x, down_y)

    def update(
        self,
        text: str = None,
        antialias: bool = None,
        color: str = None,
        alignment: str = None,
    ):
        """"""
        self.text = text if text else self.text
        self.antialias = antialias if antialias else self.antialias
        self.color = color if color else self.color
        self.alignment = alignment if alignment else self.alignment

        self.font_obj = self.render_font()
        self.x_offset, self.y_offset = self.set_alignment()
