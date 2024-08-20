"""Contains tools to works with pygame audio"""

import pygame


class Music:
    """Define music class"""

    def __init__(self) -> None:
        """Init a new music object"""
        self.music_list = {}

    def add_music(self, path: str, name: str = None):
        """Adds music to the list"""
        name = name if name else path.split(".")[0]
        self.music_list[name] = path

    def play(self, name: str, volume: float = 1, times: int = -1) -> None:
        pygame.mixer.music.load(self.music_list[name])
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(times)


class Sound:
    """Define sound class"""

    def __init__(self) -> None:
        """Init a new sound object"""
        self.sounds_list = {}

    def add_sound(self, path: str, volume: float = 1, name: str = None):
        """Adds music to the list"""
        name = name if name else path.split(".")[0]
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        self.sounds_list[name] = sound

    def play(self, name: str, volume: float = 1) -> None:
        self.sounds_list[name].play()
