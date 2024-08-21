"""Contains basic ui editing tools"""

import pygame
from utils.designer.ui_elements import Rect


class UiEditor:
    """Define main class"""

    ui_classes = {"rect": Rect}
    ui_elements = {}
    ui_groups = {}

    def create(self, data: dict) -> None:
        """Creates a new ui element"""
        base_data = data.get("base")
        element_data = data.get("element")
        text_data = data.get("text_data")

        ele_type = base_data.get("ele_type")
        group = base_data.get("group")

        element = UiEditor.ui_classes[ele_type](base_data, element_data, text_data)

        if group not in UiEditor.ui_elements:
            UiEditor.ui_elements[group] = []
            UiEditor.ui_groups[group] = True

        UiEditor.ui_elements[group].append(element)

    def draw(self) -> None:
        """Render all elements on the screen"""
        screen = pygame.display.get_surface()

        elements = [
            element
            for group, element_list in UiEditor.ui_elements.items()
            for element in element_list
            if UiEditor.ui_groups.get(group)
        ]

        for element in elements:
            if element.color == "transparent":
                continue
            pygame.draw.rect(screen, element.color, element.rect)

            screen.blit(
                element.text_obj.font_obj,
                (
                    element.rect.x + element.text_obj.x_offset,
                    element.rect.y + element.text_obj.y_offset,
                ),
            )

    def get(self, name: str) -> object:
        """Returns the given element name"""
        elements = [
            element
            for element_list in UiEditor.ui_elements.values()
            for element in element_list
        ]

        for element in elements:
            if element.name == name:
                return element

        return None

    def toggle_group(self, name: str) -> None:
        """Toggles a given group"""
        UiEditor.ui_groups[name] = not UiEditor.ui_groups[name]
