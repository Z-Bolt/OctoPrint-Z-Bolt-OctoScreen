import json


default_menu_structure = """[
    {
        "name": "Home",
        "icon": "home",
        "panel": "home"
    },
    {
        "name": "Actions",
        "icon": "actions",
        "panel": "menu",
        "items": [
            {
                "name": "Move",
                "icon": "move",
                "panel": "move"
            },
            {
                "name": "Filament",
                "icon": "filament-spool",
                "panel": "filament"
            },
            {
                "name": "Fan",
                "icon": "fan",
                "panel": "fan"
            },
            {
                "name": "Temperature",
                "icon": "heat-up",
                "panel": "temperature"
            },
            {
                "name": "Control",
                "icon": "control",
                "panel": "control"
            }
        ]
    },
    {
        "name": "Filament",
        "icon": "filament-spool",
        "panel": "filament"
    },
    {
        "name": "Configuration",
        "icon": "control",
        "panel": "menu",
        "items": [
            {
                "name": "Bed Level",
                "icon": "bed-level",
                "panel": "bed-level"
            },
            {
                "name": "ZOffsets",
                "icon": "z-offset-increase",
                "panel": "nozzle-calibration"
            },
            {
                "name": "Network",
                "icon": "network",
                "panel": "network"
            },
            {
                "name": "System",
                "icon": "info",
                "panel": "system"
            }
        ]
    }
]"""


class ZBoltOctoScreenSettings(object):
    def __init__(self, settings):
        self._settings = settings
        self.default_menu_structure = default_menu_structure

    def get_all(self):
        json_menu_structure = None
        try:
            menu_structure = self._settings.get(["menu_structure"])
            if menu_structure is None or menu_structure == "":
                menu_structure = "[]"
            json_menu_structure = json.loads(menu_structure)
        except:
            json_menu_structure = []

        return {
            "filament_in_length": float(self._settings.get(["filament_in_length"])),
            "filament_out_length": float(self._settings.get(["filament_out_length"])),
            "gcodes": self._settings.get(["gcodes"]),
            "toolchanger": bool(self._settings.get(["toolchanger"])),
            "x_axis_inverted": bool(self._settings.get(["x_axis_inverted"])),
            "y_axis_inverted": bool(self._settings.get(["y_axis_inverted"])),
            "z_axis_inverted": bool(self._settings.get(["z_axis_inverted"])),
            "menu_structure": json_menu_structure,
        }

    @staticmethod
    def default_settings():
        return dict(
            filament_in_length = 750,
            filament_out_length = 800,
            toolchanger = False,
            x_axis_inverted = False,
            y_axis_inverted = False,
            z_axis_inverted = False,
            gcodes=dict(auto_bed_level = "G29"),
            menu_structure=default_menu_structure,
        )

    @staticmethod
    def template_vars():
        return dict(default_menu_structure = default_menu_structure)
