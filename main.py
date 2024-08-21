import sys
import pygame

from utils import CONFIG
from utils.timer import SwitchTimer, RepeatedTimer, Time
from utils.mixer import Music, Sound
from utils.debbguer import Debugger
from utils.designer.ui_editor import UiEditor

from libs.movement import Movement
from libs.anim import Transition

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(CONFIG.get("window").get("size"))
pygame.display.set_caption("Souls")
clock = pygame.time.Clock()
editor = UiEditor()

editor.create(
    {
        "base": {"name": "player", "group": "gameplay", "ele_type": "rect"},
        "element": {
            "color": "red",
            "position": [5, 5],
            "size": [1, 1],
            "unit": "grid",
        },
        "text_data": {},
    }
)
editor.create(
    {
        "base": {"name": "monster1", "group": "gameplay", "ele_type": "rect"},
        "element": {
            "color": "blue",
            "position": [10, 7],
            "size": [1, 1],
            "unit": "grid",
        },
        "text_data": {},
    }
)
editor.create(
    {
        "base": {"name": "monster2", "group": "gameplay", "ele_type": "rect"},
        "element": {
            "color": "pink",
            "position": [12, 3],
            "size": [1, 1],
            "unit": "grid",
        },
        "text_data": {},
    }
)
editor.create(
    {
        "base": {"name": "battle_trans", "group": "gameplay", "ele_type": "rect"},
        "element": {
            "color": "black",
            "position": [25, 0],
            "size": [30, 25],
            "unit": "grid",
        },
        "text_data": {},
    }
)
editor.create(
    {
        "base": {"name": "test", "group": "test_group", "ele_type": "rect"},
        "element": {
            "color": "#222222",
            "position": [0, 0],
            "size": [25, 25],
            "unit": "grid",
        },
        "text_data": {},
    }
)
player = editor.get("player")
editor.toggle_group("test_group")
editor.toggle_group("test_group")

Transition.set_transition(editor.get("battle_trans"), 600, -100, duration=0.5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        Debugger.check_events(event)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Transition.start("battle_trans")
        Movement.move(player, 1, 0)
    if keys[pygame.K_LEFT]:
        Movement.move(player, -1, 0)
    if keys[pygame.K_DOWN]:
        Movement.move(player, 0, 1)
    if keys[pygame.K_UP]:
        Movement.move(player, 0, -1)

    Movement.grid_move(player, 5)
    screen.fill("white")

    editor.draw()
    Debugger.run()

    Transition.run()

    pygame.display.update()
    Time.calc_delta_time()
    clock.tick(60)
