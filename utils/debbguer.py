"""Contains debugging tools"""

import os
import pygame
from utils import CONFIG


GRID_CONFIG = CONFIG.get("grid")


class Debugger:
    """Define debugger class"""

    display_grid = True
    grid_color = GRID_CONFIG.get("color")

    step = GRID_CONFIG.get("step")
    min_div = GRID_CONFIG.get("min_div")
    max_div = GRID_CONFIG.get("max_div")
    current_div = min_div

    @staticmethod
    def check_events(event: pygame.Event) -> None:
        """Checks debugger events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                Debugger.current_div += Debugger.step
                if Debugger.current_div > Debugger.max_div:
                    Debugger.current_div = Debugger.min_div
            if event.key == pygame.K_F2:
                Debugger.current_div -= Debugger.step
                if Debugger.current_div < Debugger.min_div:
                    Debugger.current_div = Debugger.max_div
            if event.key == pygame.K_F3:
                Debugger.display_grid = not Debugger.display_grid

    @staticmethod
    def run() -> None:
        """Run debugger"""
        if Debugger.display_grid:
            Debugger.grid_drawer()

    @staticmethod
    def grid_drawer() -> None:
        """Displays a grid on the screen"""
        screen = pygame.display.get_surface()
        width, height = pygame.display.get_window_size()

        for x in range(1, Debugger.current_div):
            offset = x * (width / Debugger.current_div)
            pygame.draw.aaline(
                screen, Debugger.grid_color, (offset, 0), (offset, height)
            )

        for y in range(1, Debugger.current_div):
            offset = y * (height / Debugger.current_div)
            pygame.draw.aaline(
                screen, Debugger.grid_color, (0, offset), (width, offset)
            )
