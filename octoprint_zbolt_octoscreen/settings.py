class ZBoltSettings(object):
    def __init__(self, settings):
        self._settings = settings
    
    def get_z_offset(self, tool):
        offset = 0.0

        if tool in [1,2,3]:
            offset = self._settings.get(["t%s_offset" % tool, "z"])
        
        return float(offset)

    def set_z_offset(self, tool, value):
        # self._logger.info("Set Z Offset for T{}: {}".format(tool, value))
        self._settings.set(["t%s_offset" % tool, "z"], value)
        self._settings.save()

    def get_offsets(self):
        return [
            dict(x=0, y=0, z=0),
            dict(x=self._settings.get(["t1_offset", "x"]), y=self._settings.get(["t1_offset", "y"]), z=self._settings.get(["t1_offset", "z"])),
            dict(x=self._settings.get(["t2_offset", "x"]), y=self._settings.get(["t2_offset", "y"]), z=self._settings.get(["t2_offset", "z"])),
            dict(x=self._settings.get(["t3_offset", "x"]), y=self._settings.get(["t3_offset", "y"]), z=self._settings.get(["t3_offset", "z"]))
        ]

    def get_parking_x(self):
        return [
            self._settings.get(["parking", "t0_x"]),
            self._settings.get(["parking", "t1_x"]),
            self._settings.get(["parking", "t2_x"]),
            self._settings.get(["parking", "t3_x"])
        ]

    def get_parking_y(self):
        return self._settings.get(["parking", "y"])

    def get_parking_safe_y(self):
        return self._settings.get(["parking", "safe_y"])

    def use_sensors(self):
        return bool(self._settings.get(["parking_sensors"]))

    def use_filament_sensors(self):
        return bool(self._settings.get(["filament","sensors"]))

    @staticmethod
    def default_settings():
        return dict(
            t1_offset = dict(x=0, y=0, z=0),
            t2_offset = dict(x=0, y=0, z=0),
            t3_offset = dict(x=0, y=0, z=0),
            parking = dict(safe_y=0, y=0, t0_x=0, t1_x=0, t2_x=0, t3_x=0),
            filament = dict(
                sensors=0, 
                reservation_t0=-1,
                reservation_t1=-1,
                reservation_t2=-1,
                reservation_t3=-1
            )
        )