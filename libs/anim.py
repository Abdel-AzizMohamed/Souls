"""Contains tools to work with animation"""

from utils.timer import Time


class Transition:
    """"""

    transitions = {}

    @staticmethod
    def set_transition(
        target: object,
        start_x: int = 0,
        end_x: int = 0,
        start_y: int = 0,
        end_y: int = 0,
        duration: float = 1,
    ):
        """"""
        Transition.transitions[target.name] = {
            "target": target,
            "duration": duration,
            "start_x": start_x,
            "end_x": end_x,
            "current_x": 0,
            "start_y": start_y,
            "current_y": 0,
            "end_y": end_y,
            "running": False,
        }

    @staticmethod
    def start(name: str):
        """"""
        transition = Transition.transitions.get(name)

        transition["running"] = True
        if transition.get("start_x") != transition.get("end_x"):
            transition["current_x"] = transition.get("start_x")
        if transition.get("start_y") != transition.get("end_y"):
            transition["current_y"] = transition.get("start_y")

    @staticmethod
    def run():
        """"""
        for transition in Transition.transitions.values():
            target = transition.get("target")
            duration = transition.get("duration")

            start_x = transition.get("start_x")
            current_x = transition.get("current_x")
            end_x = transition.get("end_x")

            start_y = transition.get("start_y")
            current_y = transition.get("current_y")
            end_y = transition.get("end_y")

            if current_x == 0 and current_y == 0:
                transition["running"] = False
                target.rect.x = start_x
                target.rect.y = start_y
            if not transition.get("running"):
                continue

            if current_x:
                transition["current_x"] += Time.delta_time * (
                    end_x - start_x / duration
                )
                print(current_x)
            if current_y:
                transition["current_y"] += Time.delta_time * (
                    end_y - start_y / duration
                )

            if current_x >= end_x and start_x < end_x:
                transition["current_x"] = 0
            if current_x <= end_x and start_x > end_x:
                transition["current_x"] = 0
            if current_y >= end_y and start_y < end_y:
                transition["current_y"] = 0
            if current_y <= end_y and start_y > end_y:
                transition["current_y"] = 0

            target.rect.x = current_x
            target.rect.y = current_y
