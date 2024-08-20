import sys
import pygame

from utils import CONFIG
from utils.timer import SwitchTimer, RepeatedTimer, Time
from utils.mixer import Music, Sound
from utils.debbguer import Debugger
from utils.designer.ui_editor import UiEditor

from libs.movement import Movement

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
            "size": [4, 4],
            "unit": "grid",
        },
        "text_data": {
            "text": "Yuki chan",
            "color": "#333333",
            "size": 16,
        },
    }
)
player = editor.get("player")

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
    Time.calc_delta_time()
    pygame.display.update()
    clock.tick(60)
