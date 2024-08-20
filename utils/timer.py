import pygame
import time


class Time:
    """Contains Basic time tools"""

    delta_time = 0
    previous_time = time.time()

    @staticmethod
    def calc_delta_time():
        """Calculate deltatime"""
        Time.delta_time = time.time() - Time.previous_time
        Time.previous_time = time.time()


class Timer:
    """Timer Base class"""

    def __init__(self, time: int) -> None:
        """Init new timer object"""
        self.time = time
        self.current_time = 0
        self.end_time = 0
        self.active = False


class RepeatedTimer(Timer):
    """Define repeated timer class that works no stop"""

    def _start_timer(self) -> None:
        """Starts the timer"""
        self.active = True
        self.current_time = pygame.time.get_ticks()
        self.end_time = pygame.time.get_ticks() + self.time

    def check_timer(self) -> bool:
        """Checks if the timer has ended"""
        if not self.active:
            self._start_timer()
            return False

        if self.current_time > self.end_time:
            self.active = False
            return True

        self.current_time = pygame.time.get_ticks()


class SwitchTimer(Timer):
    """Define switch timer class that works only if active"""

    def start_timer(self) -> None:
        """Starts the timer"""
        if self.active:
            return

        self.active = True
        self.current_time = pygame.time.get_ticks()
        self.end_time = pygame.time.get_ticks() + self.time

    def check_timer(self) -> bool:
        """Checks if the timer has ended"""
        if not self.active:
            return False

        if self.current_time > self.end_time:
            self.active = False
            return True

        self.current_time = pygame.time.get_ticks()
