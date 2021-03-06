from ..sensordata import SensorData


class BatterySensor(SensorData):
    """
    Parameters
    ----------
    soc : float
            State of charge.
    u_out_inst : float
            Instantaneous output voltage of the battery.
    i_out_inst : float
            Instantaneous output current of the battery.
    temp_max : float
            Maximum temperature of the battery pack.
    temp_min : float
            Minimum temperature of the battery pack.
    """

    def __init__(self, frame, timestamp, location, rotation, soc: float, u_out_inst: float, i_out_inst: float,
                 temp_max: float, temp_min: float):
        super().__init__(frame, timestamp, location, rotation)
        self.soc = soc
        self.u_out_inst = u_out_inst
        self.i_out_inst = i_out_inst
        self.temp_max = temp_max
        self.temp_min = temp_min

    def get_dict(self) -> dict:
        battery_dict = {"frame": self.frame, "timestamp": self.timestamp,
                        "location": self.location, "rotation": self.rotation,
                        "soc": self.soc, "u_out_inst": self.u_out_inst,
                        "i_out_inst": self.i_out_inst, "temp_max": self.temp_max,
                        "temp_min": self.temp_min}
        return battery_dict
