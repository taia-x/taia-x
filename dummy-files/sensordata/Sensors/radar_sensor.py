from ..sensordata import SensorData


class RadarSensor(SensorData):
    """
    Parameters
    ----------
    altitude : float
            Altitude angle of the detection.
    azimuth : float
            Azimuth angle of the detection.
    depth : float
            Distance from the sensor to the detection position.
    velocity : float
            The velocity of the detected object towards the sensor.
    """

    def __init__(self, frame, timestamp, location, rotation, altitude: float, azimuth: float, depth: float,
                 velocity: float):
        super().__init__(frame, timestamp, location, rotation)
        self.altitude = altitude
        self.azimuth = azimuth
        self.depth = depth
        self.velocity = velocity

    def get_dict(self) -> dict:
        radar_dict = {"frame": self.frame, "timestamp": self.timestamp,
                      "location": self.location, "rotation": self.rotation,
                      "altitude": self.altitude, "azimuth": self.azimuth,
                      "depth": self.depth, "velocity": self.velocity}
        return radar_dict
