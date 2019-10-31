class ZBoltOctoScreenSettings(object):
    def __init__(self, settings):
        self._settings = settings
    

    def get_all(self):
        return {
            "filament_in_length": float(self._settings.get(["filament_in_length"])),
            "filament_out_length": float(self._settings.get(["filament_out_length"])),
            "gcodes": self._settings.get(["gcodes"]),
        }

    @staticmethod
    def default_settings():
        return dict(
            filament_in_length=750,
            filament_out_length=800,
            gcodes = dict(
                auto_bed_level="G29"
            )
        )