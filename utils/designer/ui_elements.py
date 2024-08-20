"""Contains ui elements classes"""

from utils.designer.properties import Rectangle, Text


class Base:
    """Define base ui class"""

    def __init__(self, name: str, group: str, ele_type: str) -> None:
        """Init a new base object"""

        self.name = name
        self.group = group
        self.ele_type = ele_type


class Rect(Base, Text):
    """Define basic rect shape"""

    def __init__(self, base_data: dict, rect_data: dict, text_data: dict) -> None:
        """Init a new rect object"""
        super().__init__(**base_data)

        self.color = rect_data.get("color")
        self.rect = Rectangle.create_rect(
            rect_data.get("position"), rect_data.get("size"), rect_data.get("unit")
        )
        self.text_obj = Text(self.rect, **text_data)
