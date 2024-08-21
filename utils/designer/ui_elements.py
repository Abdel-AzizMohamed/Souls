"""Contains ui elements classes"""

from utils.designer.properties import Rectangle, Text


class Base:
    """Define base ui class"""

    def __init__(self, name: str, group: str, ele_type: str) -> None:
        """Init a new base object"""

        self.name = name
        self.group = group
        self.ele_type = ele_type


class Rect(Base):
    """Define basic rect shape"""

    def __init__(self, base_data: dict, rect_data: dict, text_data: dict) -> None:
        """Init a new rect object"""
        super().__init__(**base_data)

        self.color = rect_data.get("color")
        self.rect = Rectangle.create_rect(
            rect_data.get("position"), rect_data.get("size"), rect_data.get("unit")
        )
        self.text_obj = Text(self.rect, **text_data)


class Button(Base):
    """Define basic button shape"""

    def __init__(self, base_data: dict, rect_data: dict, text_data: dict) -> None:
        """Init a new button object"""
        super().__init__(**base_data)

        self.base_color = rect_data.get("base_color")
        self.hover_color = rect_data.get("hover_color")
        self.select_color = rect_data.get("select_color")
        self.active_color = rect_data.get("base_color")

        self.rect = Rectangle.create_rect(
            rect_data.get("position"), rect_data.get("size"), rect_data.get("unit")
        )
        self.text_obj = Text(self.rect, **text_data)

    def change_state(self, state: str):
        """"""

        if state == "hover":
            self.active_color = self.hover_color
        if state == "select":
            self.active_color = self.select_color
        if state == "base":
            self.active_color = self.base_color
