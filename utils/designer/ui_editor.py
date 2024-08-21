"""Contains basic ui editing tools"""

import pygame
from utils.designer.ui_elements import Rect, Button
from utils.importer import import_callable


class UiEditor:
    """Define main class"""

    ui_classes = {"rect": Rect, "button": Button}
    ui_elements = {}
    ui_groups = {}

    def create(self, data: dict) -> None:
        """Creates a new ui element"""
        base_data = data.get("base")
        element_data = data.get("element")
        text_data = data.get("text_data")
        event_data = data.get("event_data")

        ele_type = base_data.get("ele_type")
        group = base_data.get("group")

        element = UiEditor.ui_classes[ele_type](base_data, element_data, text_data)
        self.set_events(element, event_data)

        if group not in UiEditor.ui_elements:
            UiEditor.ui_elements[group] = []
            UiEditor.ui_groups[group] = True

        UiEditor.ui_elements[group].append(element)

    def set_events(self, element: object, event_data: dict):
        """"""
        for name, data in event_data.items():
            Events.add_event(element, name, **data)

        if element.ele_type == "button":
            Events.add_event(
                element,
                "base",
                "mouseout",
                "utils.designer.ui_elements:Button.change_state",
                ["base"],
            )
            Events.add_event(
                element,
                "hover",
                "mousein",
                "utils.designer.ui_elements:Button.change_state",
                ["hover"],
            )
            Events.add_event(
                element,
                "select",
                "leftclick",
                "utils.designer.ui_elements:Button.change_state",
                ["select"],
            )

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
            if element.ele_type == "rect":
                if element.color == "transparent":
                    continue
                pygame.draw.rect(screen, element.color, element.rect)

            if element.ele_type == "button":
                pygame.draw.rect(screen, element.active_color, element.rect)

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


class Events:
    """Define ui events class"""

    elements_events = {}

    @staticmethod
    def add_event(
        element: object, name: str, event: str, callable_path: str, args: list
    ):
        """"""
        callable = import_callable(element, callable_path)
        Events.elements_events[f"{element.name}_{name}"] = {
            "target": element,
            "event": event,
            "callable": callable,
            "args": args,
        }

    @staticmethod
    def run(event_handler: pygame.Event):
        """Run all events"""
        events = [
            event
            for event in Events.elements_events.values()
            if UiEditor.ui_groups.get(event.get("target").group)
            and getattr(event.get("target"), "disabled", "None")
        ]

        for event in events:
            if event.get("event") in {"leftclick", "rightclick", "middleclick"}:
                Events.check_mouse(event, event_handler)
            if event.get("event") in {"mousein", "mouseout"}:
                Events.check_collision(event, event_handler)

    @staticmethod
    def check_mouse(event: dict, event_handler: pygame.Event):
        """Checks for mouse events"""
        mouse_id = {"leftclick": 0, "middleclick": 1, "rightclick": 2}

        if pygame.mouse.get_pressed()[mouse_id.get(event.get("event"))]:
            event.get("callable")(*event.get("args"))

    def check_collision(event: dict, event_handler: pygame.Event):
        if (
            event.get("target").rect.collidepoint(pygame.mouse.get_pos())
            and event.get("event") == "mousein"
        ):
            event.get("callable")(*event.get("args"))

        if (
            not event.get("target").rect.collidepoint(pygame.mouse.get_pos())
            and event.get("event") == "mouseout"
        ):
            event.get("callable")(*event.get("args"))
